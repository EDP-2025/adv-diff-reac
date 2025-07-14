#!/usr/bin/env python3
import os
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

# Directorio raíz y carpeta de resultados
top = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RESULTS_DIR = os.path.join(top, 'results')
os.makedirs(RESULTS_DIR, exist_ok=True)

# Funciones auxiliares
def fuente(t, X, Y):
    return (1 + t) * np.sin(np.pi * X) * np.sin(np.pi * Y)
    # return np.zeros_like(X)

def cond_inic(X, Y):
    return np.exp(-50 * ((X - 0.5)**2 + (Y - 0.5)**2))

def aplicar_bc(u, nx, ny):
    uma = u.reshape(nx, ny)
    uma[0, :] = uma[-1, :] = uma[:, 0] = uma[:, -1] = 0
    return uma.ravel()

def Vx_func(t, X, Y, Tfin):
    return 1.0 + 0.5 * np.sin(2 * np.pi * t / Tfin) * X
    # return np.ones_like(X) * 1

def Vy_func(t, X, Y, Tfin):
    return 0.5 + 0.25 * np.cos(2 * np.pi * t / Tfin) * Y
    # return np.ones_like(Y) * 0.5


# Ensamblaje de A
def montarA(Vx, Vy, nx, ny, dx, dy, D, k):
    N = nx * ny
    A = sp.lil_matrix((N, N))
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            p = i*ny + j
            A[p, p] = (-Vx[i,j]/dx - Vy[i,j]/dy - 2*D*(1/dx**2 + 1/dy**2) - k)
            A[p, (i-1)*ny + j] = Vx[i,j]/dx + D/dx**2
            A[p, (i+1)*ny + j] = D/dx**2
            A[p, i*ny + (j-1)] = Vy[i,j]/dy + D/dy**2
            A[p, i*ny + (j+1)] = D/dy**2
    return A.tocsc()

# Función principal FDM 
def solve_fdm(nx, ny, Lx, Ly, Tfin, D, k, theta, dt_factor, fuente_func=fuente):
    dx = Lx / (nx - 1)
    dy = Ly / (ny - 1)
    x = np.linspace(0, Lx, nx)
    y = np.linspace(0, Ly, ny)
    X, Y = np.meshgrid(x, y, indexing='ij')

    dt_diff = 1.0 / (2*D*(1/dx**2 + 1/dy**2)) if D>0 else np.inf
    Vx0 = np.max(Vx_func(0, X, Y, Tfin))
    Vy0 = np.max(Vy_func(0, X, Y, Tfin))
    dt_adv = min(dx/Vx0, dy/Vy0)
    dt = dt_factor * min(dt_diff, dt_adv)

    pasos = int(np.ceil(Tfin / dt))
    U = np.zeros((pasos+1, nx, ny))
    u = aplicar_bc(cond_inic(X, Y).ravel(), nx, ny)
    U[0] = u.reshape(nx, ny)

    for n in range(1, pasos+1):
        t_n = (n-1) * dt
        t_np = n * dt
        Vx_n = Vx_func(t_n,  X, Y, Tfin)
        Vy_n = Vy_func(t_n,  X, Y, Tfin)
        Vx_p = Vx_func(t_np, X, Y, Tfin)
        Vy_p = Vy_func(t_np, X, Y, Tfin)

        A_n = montarA(Vx_n, Vy_n, nx, ny, dx, dy, D, k)
        A_p = montarA(Vx_p, Vy_p, nx, ny, dx, dy, D, k)

        I  = sp.eye(nx*ny, format='csc')
        M1 = (I - theta*dt*A_p).tocsc()
        M2 = (I + (1-theta)*dt*A_n).tocsc()

        F_n = fuente_func(t_n, X, Y).ravel()
        F_p = fuente_func(t_np, X, Y).ravel()

        rhs = M2.dot(u) + dt*((1-theta)*F_n + theta*F_p)
        u   = spla.spsolve(M1, rhs)
        u   = aplicar_bc(u, nx, ny)

        U[n] = u.reshape(nx, ny)

    return U, X, Y, dt

# Animación con vectores
def animate_fdm(U, X, Y, dt, Tfin, filename="animacion5_fdm.gif", skip=10, fps=20):
    vmin, vmax = U.min(), U.max()
    frames = range(0, U.shape[0], skip)
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    def update(i):
        ax.clear()
        t = frames[i] * dt
        # Contorno
        ax.contourf(X, Y, U[frames[i]], 20, vmin=vmin, vmax=vmax)
        # Vectores de velocidad
        Vx = Vx_func(t, X, Y, Tfin)
        Vy = Vy_func(t, X, Y, Tfin)
        ax.quiver(X, Y, Vx, Vy, color="white", scale=15, width=0.002)
        ax.set_title(f"t = {t:.3f}")
        return []
    ani = animation.FuncAnimation(fig, update, frames=len(frames), blit=False)
    fullpath = os.path.join(RESULTS_DIR, filename)
    writer = PillowWriter(fps=fps)
    ani.save(fullpath, writer=writer)
    print(f"GIF guardado en: {fullpath}")

# Prueba rápida
if __name__ == "__main__":
    nx, ny, Lx, Ly = 16, 16, 1.0, 1.0
    Tfin, D, k = 1.0, 0.5, 0.5
    theta, dt_factor = 0.5, 0.01
    U, X, Y, dt = solve_fdm(nx, ny, Lx, Ly, Tfin, D, k, theta, dt_factor)
    animate_fdm(U, X, Y, dt, Tfin)

# src/fdm.py
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

# === Helper functions ===
def fuente(t, X, Y):
    return np.zeros_like(X)

def cond_inic(X, Y):
    return np.exp(-50 * ((X - 0.5)**2 + (Y - 0.5)**2))

def aplicar_bc(u):
    u[0, :] = 0; u[-1, :] = 0; u[:, 0] = 0; u[:, -1] = 0
    return u

def Vx_func(t, X, Y):
    return np.ones_like(X)

def Vy_func(t, X, Y):
    return 0.01 * np.ones_like(Y)

def montarA(Vx, Vy, nx, ny, dx, dy, D, k):
    N = nx * ny
    A = sp.lil_matrix((N, N))
    for i in range(nx):
        for j in range(ny):
            p = i*ny + j
            if i in (0, nx-1) or j in (0, ny-1):
                continue
            A[p, p] = (-Vx[i,j]/dx - Vy[i,j]/dy)
            A[p, p] += -2*D*(1/dx**2 + 1/dy**2) - k
            A[p, (i-1)*ny + j] = Vx[i,j]/dx + D/dx**2
            A[p, (i+1)*ny + j] = D/dx**2
            A[p, i*ny + (j-1)] = Vy[i,j]/dy + D/dy**2
            A[p, i*ny + (j+1)] = D/dy**2
    return A.tocsc()

# === Función principal de FDM ===
def solve_fdm(nx, ny, Lx, Ly, Tfin, D, k, theta, dt_factor):
    """
    Corre el método theta (FDM) de advección–difusión–reacción
    y devuelve la matriz U[timestep, i, j], la malla X, Y y dt real.
    """
    dx = Lx / (nx - 1); dy = Ly / (ny - 1)
    x = np.linspace(0, Lx, nx); y = np.linspace(0, Ly, ny)
    X, Y = np.meshgrid(x, y, indexing='ij')
    Vx0 = np.max(Vx_func(0, X, Y)); Vy0 = np.max(Vy_func(0, X, Y))

    # Determina dt usando CFL
    dt_diff = 1.0 / (2*D*(1/dx**2 + 1/dy**2))
    dt_adv  = min(dx/Vx0, dy/Vy0)
    dt      = dt_factor * min(dt_diff, dt_adv)

    pasos = int(np.ceil(Tfin / dt))
    U = np.zeros((pasos+1, nx, ny))
    u = aplicar_bc(cond_inic(X, Y)).ravel()
    U[0] = u.reshape(nx, ny)

    t = 0.0
    for n in range(1, pasos+1):
        Vx = Vx_func(t, X, Y); Vy = Vy_func(t, X, Y)
        A  = montarA(Vx, Vy, nx, ny, dx, dy, D, k)
        I  = sp.eye(nx*ny, format='csc')

        M1 = (I - theta*dt*A).tocsc()
        M2 = (I + (1-theta)*dt*A).tocsc()
        F_n   = fuente(t,    X, Y).ravel()
        F_np1 = fuente(t+dt, X, Y).ravel()

        rhs = M2.dot(u) + dt*((1-theta)*F_n + theta*F_np1)
        u   = spla.spsolve(M1, rhs)
        u   = aplicar_bc(u.reshape(nx, ny)).ravel()
        U[n] = u.reshape(nx, ny)
        t   += dt

    return U, X, Y, dt

# === Función para animar y guardar GIF ===
# En src/fdm.py, reemplaza animate_fdm por esto:

def animate_fdm(U, X, Y, dt, filename="animacion_fdm.gif",
                skip=10, fps=20):
    """
    Crea un GIF submuestreando la solución cada `skip` pasos y
    reproduciéndolo a `fps` cuadros por segundo.
    """
    U0max = U.max()
    U0min = U.min()
    fig, ax = plt.subplots()
    
    # Aquí tomamos solo cada `skip`-ésimo fotograma
    frames = range(0, U.shape[0], skip)
    
    def init():
        ax.clear()
        cf = ax.contourf(X, Y, U[0], 20, vmin=U0min, vmax=U0max)
        ax.set_title("t = 0")
        return []
    
    def anim(i):
        ax.clear()
        t = frames[i] * dt
        cf = ax.contourf(X, Y, U[frames[i]], 20,
                         vmin=U0min, vmax=U0max)
        ax.set_title(f"t = {t:.3f}")
        return []
    
    ani = animation.FuncAnimation(
        fig, anim,
        frames=len(frames),
        init_func=init,
        blit=False
    )
    writer = PillowWriter(fps=fps)
    ani.save(filename, writer=writer)
    print(f"GIF saved as {filename}")


# === Prueba rápida ===
if __name__ == "__main__":
    # Parámetros de ejemplo
    nx, ny    = 16, 16
    Lx, Ly    = 1.0, 1.0
    Tfin      = 0.1
    D, k      = 0.5, 0.5
    theta     = 0.5
    dt_factor = 0.01

    U, X, Y, dt = solve_fdm(nx, ny, Lx, Ly, Tfin, D, k, theta, dt_factor)
    animate_fdm(U, X, Y, dt)

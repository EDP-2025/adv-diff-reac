# src/fem.py
#!/usr/bin/env python3
import os
import numpy as np
import matplotlib.pyplot as plt

from skfem import MeshTri, ElementTriP1, Basis, asm
from skfem.assembly import BilinearForm, LinearForm
from skfem.helpers import grad, dot
from scipy.sparse.linalg import spsolve
from matplotlib.animation import FuncAnimation, PillowWriter

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RESULTS_DIR = os.path.join(BASE, 'results')
os.makedirs(RESULTS_DIR, exist_ok=True)


# FUNCIONES PRINCIPALES DE FEM
def solve_fem(nx, ny, Lx, Ly, Tfin, D, k, theta=0.5, dt=0.01):
    # Parámetros de mallado y tiempo
    nt = int(np.ceil(Tfin / dt))
    x = np.linspace(0.0, Lx, nx)
    y = np.linspace(0.0, Ly, ny)
    mesh = MeshTri.init_tensor(x, y)
    element = ElementTriP1()
    basis = Basis(mesh, element)

    # Formas bilineales espaciales
    @BilinearForm
    def masa(u, v, w):
        return u * v

    @BilinearForm
    def rigidez(u, v, w):
        return dot(grad(u), grad(v))

    @BilinearForm
    def reaccion(u, v, w):
        return k * u * v

    # Ensamblaje de matrices constantes
    M = asm(masa, basis)
    K = D * asm(rigidez, basis)
    R = asm(reaccion, basis)

    # Funciones dependientes de t
    def ensamblar_adveccion(t):
        @BilinearForm
        def adveccion(u, v, w):
            xq, yq = w.x
            Vx = 1.0 + 0.5 * np.sin(2*np.pi * t/Tfin) * xq
            Vy = 0.5 + 0.25 * np.cos(2*np.pi * t/Tfin) * yq
            return (Vx * grad(u)[0] + Vy * grad(u)[1]) * v
        return asm(adveccion, basis)

    def ensamblar_fuente(t):
        @LinearForm
        def fuente(v, w):
            xq, yq = w.x
            #return (1 + t) * np.sin(np.pi * xq) * np.sin(np.pi * yq) * v
            return 0 * v
        return asm(fuente, basis)

    # Condiciones de contorno e inicial
    N = M.shape[0]
    X, Y = mesh.p
    dofs_bdy = np.where((X == 0.0) | (X == Lx) | (Y == 0.0) | (Y == Ly))[0]
    all_dofs = np.arange(N)
    dofs_free = np.setdiff1d(all_dofs, dofs_bdy)

    def cond_inic_xy(x, y):
        return np.exp(-50 * ((x - Lx/2)**2 + (y - Ly/2)**2))

    u = cond_inic_xy(X, Y)
    u[dofs_bdy] = 0.0

    # Almacenar solución
    U = np.zeros((nt+1, N))
    U[0] = u.copy()

    # Bucle temporal método theta
    for n in range(nt):
        t_n = n * dt
        t_np1 = (n+1) * dt

        A_n = ensamblar_adveccion(t_n)
        A_np1 = ensamblar_adveccion(t_np1)
        C_n = A_n + R
        C_np1 = A_np1 + R

        F_n = ensamblar_fuente(t_n)
        F_np1 = ensamblar_fuente(t_np1)

        lhs = M + theta * dt * (K + C_np1)
        rhs = M - (1 - theta) * dt * (K + C_n)

        # Restringir a nodos libres
        lhs_f = lhs[dofs_free][:, dofs_free]
        b = rhs.dot(u) + dt * ((1-theta) * F_n + theta * F_np1)
        b_free = b[dofs_free]

        # Resolver y reconstruir
        u_free = spsolve(lhs_f, b_free)
        u = np.zeros(N)
        u[dofs_free] = u_free
        U[n+1] = u.copy()

    return U, X, Y, mesh, dt


def animate_fem(U, X, Y, mesh, dt, Tfin, Lx, Ly,
                filename="animacion_fem.gif", skip=1, fps=5):
    vmin, vmax = U.min(), U.max()
    frames = list(range(0, U.shape[0], skip))

    fig, ax = plt.subplots(figsize=(5,4))
    ax.set_aspect('equal')

    def update(i):
        ax.clear()
        t = frames[i] * dt
        ax.tricontourf(
            X, Y, mesh.t.T, U[frames[i]],
            levels=20, vmin=vmin, vmax=vmax
        )
        #Vx = np.ones_like(X) * 1.0
        #Vy = np.ones_like(Y) * 0.5
        Vx = 1.0 + 0.5 * np.sin(2*np.pi * t/Tfin) * X
        Vy = 0.5 + 0.25 * np.cos(2*np.pi * t/Tfin) * Y
        ax.quiver(X, Y, Vx, Vy, color="white", scale=15, width=0.002)
        ax.set_title(f"t = {t:.3f}")
        ax.set_xticks([0, Lx/2, Lx])
        ax.set_yticks([0, Ly/2, Ly])
        return []

    ani = FuncAnimation(fig, update, frames=len(frames), blit=False)
    writer = PillowWriter(fps=fps)
    fullpath = os.path.join(RESULTS_DIR, filename)
    ani.save(fullpath, writer=writer)
    print(f"GIF guardado en: {fullpath}")
    


if __name__ == "__main__":
    # Ejecución de prueba
    params = dict(nx=16, ny=16, Lx=1.0, Ly=1.0,
                  Tfin=1, D=0.00, k=0.01, theta = 0.5, dt = 0.01)
    U, X, Y, mesh, dt = solve_fem(**params)
    skip = 1
    fps = 5
    animate_fem(U, X, Y, mesh, dt,
                params['Tfin'], params['Lx'], params['Ly'],
                filename="animacion_casoprueba.gif",
                skip=skip,
                fps=fps
                )
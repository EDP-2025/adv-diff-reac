# src/adv_diff_reac.py
"""
Script que corre tanto FDM como FEM y compara resultados.
"""

from fdm import solve_fdm, animate_fdm
from fem import solve_fem

def main():
    # Parámetros comunes
    nx, ny    = 16, 16
    Lx, Ly    = 1.0, 1.0
    Tfin      = 0.1
    D, k      = 0.5, 0.5
    theta     = 0.5
    dt_factor = 0.01

    # FDM
    U, X, Y, dt = solve_fdm(nx, ny, Lx, Ly, Tfin, D, k, theta, dt_factor)
    animate_fdm(U, X, Y, dt, filename="results/anim_fdm.gif")

    # FEM (aún no implementado)
    try:
        u_fem = solve_fem(nx, ny, Lx, Ly, Tfin, D, k)
        # aquí podrías plotear u_fem...
    except NotImplementedError as e:
        print(e)

if __name__ == "__main__":
    main()

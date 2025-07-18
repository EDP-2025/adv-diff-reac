# src/adv_diff_reac.py
"""
Script que corre tanto FDM como FEM 
"""

from fdm   import solve_fdm, animate_fdm
from fem   import solve_fem, animate_fem 

def main():
    nx, ny = 16, 16
    Lx, Ly = 1.0, 1.0
    Tfin = 0.1
    D, k = 0.5, 0.5
    theta = 0.5
    dt_factor = 0.01

    # FDM
    U_fdm, X_fdm, Y_fdm, dt_fdm = solve_fdm(
        nx, ny, Lx, Ly, Tfin, D, k, theta, dt_factor
    )
    # Asegurarse de que la carpeta results/ existe
    animate_fdm(
        U_fdm, X_fdm, Y_fdm, dt_fdm, Tfin, 
        filename="anim_fdm.gif"
    )

    # FEM
    # solve_fem devuelve U, X, Y, mesh, dt
    U_fem, X_fem, Y_fem, mesh, dt_fem = solve_fem(
        nx, ny, Lx, Ly, Tfin, D, k, theta, dt=dt_factor
    )
    animate_fem(
        U_fem, X_fem, Y_fem, mesh, dt_fem,
        Tfin, Lx, Ly,
        filename="anim_fem.gif"
    )


if __name__ == "__main__":
    main()

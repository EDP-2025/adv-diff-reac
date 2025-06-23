# src/adv_diff_reac_solver.py
"""
Solución numérica del problema de advección-difusión-reacción
en 2D usando:
  - Método de diferencias finitas (FDM)
  - Método de elementos finitos (FEM)
"""

import numpy as np
import matplotlib.pyplot as plt
# from skfem import MeshTri, ElementTriP1, Basis  # si usarás scikit-fem

def solve_fdm(nx, ny, Lx, Ly, dt, T, params):
    """
    Implementa aquí tu esquema FDM.
    Parámetros:
      nx, ny : número de nodos en x e y
      Lx, Ly : dimensiones del dominio
      dt, T  : paso de tiempo y tiempo final
      params : diccionario con coeficientes de advección, difusión y reacción
    Retorna:
      u : solución en el último instante
    """
    # TODO: montar malla, matrices, iterar en t…
    return None

def solve_fem(nx, ny, Lx, Ly, dt, T, params):
    """
    Implementa aquí tu esquema FEM.
    """
    # TODO: generar malla triangular, ensamblar, resolver…
    return None

def plot_solution(u, X, Y):
    """Función para graficar el campo u(x,y)."""
    plt.figure()
    cp = plt.contourf(X, Y, u, 20)
    plt.colorbar(cp)
    plt.xlabel('x'); plt.ylabel('y');
    plt.title('Solución en t final')
    plt.show()

if __name__ == "__main__":
    # Parámetros de ejemplo
    nx, ny = 50, 50
    Lx, Ly = 1.0, 1.0
    dt, T    = 0.001, 0.1
    params = {'v': (1.0, 0.5), 'D': 0.01, 'k': 1.0}

    # Malla para graficar
    x = np.linspace(0, Lx, nx)
    y = np.linspace(0, Ly, ny)
    X, Y = np.meshgrid(x, y)

    # Llamadas (por ahora devuelven None)
    u_fdm = solve_fdm(nx, ny, Lx, Ly, dt, T, params)
    u_fem = solve_fem(nx, ny, Lx, Ly, dt, T, params)

    # Ejemplo de plot (una vez implementado)
    # plot_solution(u_fdm, X, Y)

# EDP Advección–Difusión–Reacción Solver

## Descripción

Este repositorio implementa un solver numérico para la ecuación de advección–difusión–reacción en un dominio rectangular 2D.

### Ecuación a resolver

```math
\frac{\partial c}{\partial t} + A[c](t,x,y) = f(t,x,y), \quad
A[c](t,x,y) = \mathbf{V}(t,x,y)\cdot\nabla c - D\Delta c + \kappa c
```

Con condiciones de contorno Dirichlet homogéneas:

```math
c(t,x,y) = 0 \quad \text{en } \partial([0,L_x]\times[0,L_y]), \forall t\in[0,T]
```

Condición inicial:

```math
c(0,x,y) = c_0(x,y)
```

Parámetros dados: \$D\$, \$\kappa\$, funciones \$\mathbf{V}(t,x,y)\$, \$f(t,x,y)\$ y \$c\_0(x,y)\$.

## Estructura del proyecto

```
adf-diff-reac/
├── src/            # Código fuente Python (fdm.py, fem.py, adv_diff_reac.py)
├── notebooks/      # Jupyter Notebooks de pruebas y exploraciones
├── results/        # Figuras, animaciones y datos de salida
├── docs/           # Documentación adicional
├── .gitignore      # Archivos ignorados por Git
├── requirements.txt# Dependencias Python
└── README.md       # Documentación del proyecto
```

## Instalación

```bash
git clone https://github.com/EDP-2025/adv-diff-reac.git
cd adv-diff-reac
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Uso

Ejecuta el script principal:

```bash
python src/adv_diff_reac.py
```

* Genera la animación FDM en `results/anim_fdm.gif`.
* Placeholder FEM imprime “solve\_fem aún no implementado”.

## Etapas del trabajo

1. **FDM**: Implementación y resultados.
2. **FEM**: Implementación con elementos de orden 1 y triangulación predefinida.

- [Enunciado y etapas](docs/problema.md) – fórmula, BC, CI y desglose de tareas.
- [Resultados FDM](docs/resultados_fdm.md) – animaciones y conclusiones de los distintos casos.


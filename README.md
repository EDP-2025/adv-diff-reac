# Solver de la EDP de Advección–Difusión–Reacción 
**Autora:** Gabriela Gutiérrez  
**Fecha:** Junio 2025  

## Descripción

Este repositorio implementa un solver numérico para la ecuación de advección–difusión–reacción en un dominio rectangular 2D.

### Ecuación a resolver

```math
\frac{\partial c}{\partial t} + A[c](t,x,y) = f(t,x,y), \quad
A[c](t,x,y) = \mathbf{V}(t,x,y)\cdot\nabla c - D\Delta c + \kappa c
```

con \$(t,x,y)\in [0,T]\times [0,L_{x}]\times [0,L_{y}]\$.

Con condiciones de contorno Dirichlet homogéneas:

```math
c(t,x,y) = 0 \quad (t, x, y) \in \partial([0,L_{x}]\times[0,L_{y}]), \forall t\in[0,T]
```

Condición inicial:

```math
c(0,x,y) = c_0(x,y)
```

Parámetros dados: \$D\$, \$\kappa\$, funciones \$\mathbf{V}(t,x,y)\$, \$f(t,x,y)\$ y \$c\_0(x,y)\$.

## Resumen de resultados

En este proyecto implementamos y comparamos dos técnicas numéricas para resolver la ecuación de advección–difusión–reacción en 2D:

1. **Método de Diferencias Finitas (FDM)**  
2. **Método de Elementos Finitos P1 (FEM)**  

A partir de un **pulso gaussiano** inicial centrado en \$(0.5,0.5)\$, las animaciones en `results/` ilustran:

- **Transporte**: cómo el pulso viaja a lo largo del dominio arrastrado por el campo de velocidades \$\mathbf V(t,x,y)\$.  
- **Difusión**: ensanchamiento gradual de la campana según el coeficiente \$D\$.  
- **Reacción**: atenuación exponencial de la amplitud con el parámetro \$k\$.  

---

### Ejemplos de salidas

<p align="center">
  <img src="results/animacion_caso2_fdm.gif" alt="Animación FDM" width="320"/>
  &nbsp;&nbsp;
  <img src="results/animacion_caso2_fem.gif" alt="Animación FEM" width="300"/>
</p>

- **FDM** (`animacion_caso2_fdm.gif`):  
    Se observa como la campana se ensancha por difusión, se desplaza arrastrada por el campo de velocidades y va perdiendo altura de forma suave por el término de reacción

- **FEM** (`animacion_caso2_fem.gif`):  
    Muestra el mismo experimento con elementos finitos P1. La onda inicial se difunde en el espacio, viaja según el flujo dinámico y se diluye gradualmente por la reacción.

---

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
* Genera la animación FEM en `results/anim_fem.gif`.

## Etapas del trabajo

1. **FDM**: Implementación y resultados.
2. **FEM**: Implementación con elementos de orden 1 y triangulación predefinida.

- [Enunciado y etapas](docs/problema.md) – fórmula, BC, CI y desglose de tareas.
- [Resultados FDM](docs/resultados_fdm.md) – animaciones y conclusiones de los distintos casos haciendo uso del método de diferencias finitas.
- [Resultados FEM](docs/resultados_fem.md) – animaciones y conclusiones de los distintos casos haciendo uso del método de elementos finitos.


## Referencias

Consulta todas las referencias en [docs/referencias.md](docs/referencias.md).


- [AUTHORS](AUTHORS.md) – Lista de autores y contribuciones.

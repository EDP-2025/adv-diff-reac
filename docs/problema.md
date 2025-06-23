# Enunciado del Problema

Durante este semestre trabajaremos en la solución numérica de la ecuación de  
advección–difusión–reacción en un dominio rectangular 2D:

```math
\frac{\partial c}{\partial t} + A[c](t,x,y) = f(t,x,y),
\quad
A[c] = \mathbf{V}(t,x,y)\cdot\nabla c - D\Delta c + \kappa\,c
```
con  
```math
c=0\quad\text{en } \partial([0,L_x]\times[0,L_y]),\quad
c(0,x,y)=c_0(x,y),
```
donde $D,\kappa\in\mathbb{R}$ y $\mathbf{V},f,c_0$ son funciones dadas.  

El trabajo se divide en dos etapas:  
1. Implementar un método apropiado de **Diferencias Finitas** y presentar resultados.  
2. Implementar el método de **Elementos Finitos**, con polinomios de orden $1$ con la triangulaci ́on que aparece en la siguiente figura:
![Triangulación en elementos lineales](../results/Malla.png)



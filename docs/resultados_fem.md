# Resultados del Método de Elementos Finitos

En esta sección presentamos los resultados obtenidos al resolver numéricamente la ecuación de advección–difusión–reacción  
```math
\frac{\partial c}{\partial t} + \mathbf V(t,x,y)\cdot\nabla c \;-\; D\,\Delta c \;+\;\kappa\,c \;=\; f(t,x,y),
```
en el dominio \$[0,T]\times[0,L_x]\times[0,L_y]\$, con condiciones de contorno de Dirichlet homogéneas  
```math
c(t,x,y) = 0
\quad\forall\,(t,x,y)\in\partial\bigl([0,L_x]\times[0,L_y]\bigr),\;\forall\,t\in[0,T],
```
y condición inicial  
```math
c(0,x,y) \;=\; c_0(x,y).
```

Como condición inicial específica, hemos considerado un **pulso gaussiano** centrado en \((0.5,0.5)\):  
```math
c_0(x,y) \;=\; \exp\bigl(-50\bigl[(x-0.5)^2 + (y-0.5)^2\bigr]\bigr).
```

discretizado con elementos finitos P1 sobre malla triangular y tiempo integrado con θ-method (θ = 0.5, Crank–Nicolson).

---

## Caso 1: Sin difusión  
**Parámetros**  
- D = 0  
- k = 0.01
- f = 0  
- Vx = 1.0 + 0.5 sin(2π t/Tfin) X  
- Vy = 0.5 + 0.25 cos(2π t/Tfin) Y  

![Animación 1: Sin difusión](../results/animacion_caso1_fem.gif)

**Conclusión**  
Con D=0, el esquema FEM transporta la gaussiana sin cambiar su forma ni anchura. Sólo pierde un poco de altura al tocar los bordes, por las condiciones de contorno.


---

## Caso 2: Difusión moderada  
**Parámetros**  
- D = 0.05
- k = 0.01
- f = 0  
- Vx = 1.0 + 0.5 sin(2π t/Tfin) X  
- Vy = 0.5 + 0.25 cos(2π t/Tfin) Y  

![Animación 2: Difusión moderada](../results/animacion_caso2_fem.gif)

**Conclusión**  


Con D=0.5 la difusión hace que la gaussiana se “extienda”: la cresta se aplana y el pulso se hace más ancho con el tiempo, mostrando el efecto disipativo del término Δu.

---

## Caso 3: Reacción fuerte  
**Parámetros**  
- D = 0.05
- k = 5
- f = 0  
- Vx = 1.0 + 0.5 sin(2π t/Tfin) X  
- Vy = 0.5 + 0.25 cos(2π t/Tfin) Y  

![Animación 3: Reacción fuerte](../results/animacion_caso3_fem.gif)

**Conclusión**  
Al aumentar k a 100, el término de reacción “absorbe” la gaussiana casi de inmediato: la amplitud cae rápidamente y la curva desaparece casi por completo.

---

## Caso 4: Fuente activada  
**Parámetros**  
- D = 0.05
- k = 0.01 
- f(t,x,y) = (1 + t) sin(πx) sin(πy)  
- Vx = 1.0 + 0.5 sin(2π t/Tfin) X  
- Vy = 0.5 + 0.25 cos(2π t/Tfin) Y  

![Animación 4: Fuente activada](../results/animacion_caso4_fem.gif)

**Conclusión**  
Con la fuente no homogénea, la fuente introduce energía en el centro del dominio. Al principio la onda crece ahí, luego la difusión y la reacción equilibran la producción y se forma un perfil casi estable parecido a la función fuente.

---

## Caso 5: Campo constante  
**Parámetros**  
- D = 0.05
- k = 0.01 
- f = 0  
- Vx = 1.0 (constante)  
- Vy = 0.5 (constante)  

![Animación 5: Campo constante](../results/animacion_caso5_fem.gif)

**Conclusión**  
Con velocidades constantes la onda se desplaza de manera uniforme sin deformarse por variaciones del campo. La difusión sigue aplanando la cresta, pero el movimiento es lineal y predecible.

---

**Comentarios generales sobre el método de diferencias finitas**  
- El método θ (θ=0.5) combina estabilidad y precisión de segundo orden en el tiempo.  
- La difusión (D) controla cuánto se dispersa el pulso.  
- La reacción (k) regula la velocidad de amortiguación de la solución.  
- La fuente añade o retira energía según su forma.  
- Comparado con diferencias finitas, FEM con elementos P1 en malla triangular ofrece soluciones suaves y sin sesgo direccional, aunque ambos métodos muestran resultados muy parecidos en este dominio rectangular.  

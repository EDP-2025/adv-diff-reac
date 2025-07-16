# Resultados del Método de Diferencias Finitas

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

La discretización combina diferencias finitas en el espacio con el **θ–method** en el tiempo (θ = 0.5, Crank–Nicolson).  


---

## Caso 1: Sin difusión  
**Parámetros**  
- D = 0  
- k = 0.01
- f = 0  
- Vx = 1.0 + 0.5 sin(2π t/Tfin) X  
- Vy = 0.5 + 0.25 cos(2π t/Tfin) Y  

![Animación 1: Sin difusión](../results/animacion_caso1_fdm.gif)

**Conclusión**  
Al anular D, el término de difusión desaparece y la solución se transporta prácticamente sin cambio de forma: el pico de la gaussiana mantiene su altura mientras se desplaza, salvo pequeñas pérdidas en los bordes impuestas por las condiciones de contorno Dirichlet.

---

## Caso 2: Difusión moderada  
**Parámetros**  
- D = 0.05
- k = 0.01
- f = 0  
- Vx = 1.0 + 0.5 sin(2π t/Tfin) X  
- Vy = 0.5 + 0.25 cos(2π t/Tfin) Y  

![Animación 2: Difusión moderada](../results/animacion_caso2_fdm.gif)

**Conclusión**  
Con D=0.5 la difusión suaviza rápidamente la curva: los gradientes se atenúan, la cresta se aplana y la anchura de la gaussiana aumenta, demostrando el papel disipativo del término Δu en el esquema de diferencias finitas.

---

## Caso 3: Reacción fuerte  
**Parámetros**  
- D = 0.05
- k = 5
- f = 0  
- Vx = 1.0 + 0.5 sin(2π t/Tfin) X  
- Vy = 0.5 + 0.25 cos(2π t/Tfin) Y  

![Animación 3: Reacción fuerte](../results/animacion_caso3_fdm.gif)

**Conclusión**  
Al aumentar k a 100, el término de reacción domina y provoca una aniquilación rápida de la onda: la amplitud decae casi instantáneamente, mostrando el carácter fuertemente disipativo de –k u en la EDP.

---

## Caso 4: Fuente activada  
**Parámetros**  
- D = 0.05
- k = 0.01 
- f(t,x,y) = (1 + t) sin(πx) sin(πy)  
- Vx = 1.0 + 0.5 sin(2π t/Tfin) X  
- Vy = 0.5 + 0.25 cos(2π t/Tfin) Y  

![Animación 4: Fuente activada](../results/animacion_caso4_fdm.gif)

**Conclusión**  
Con la fuente no homogénea, la solución crece en las zonas de inyección (\(\sinπx\sinπy\)) y luego alcanza un estado pseudo–estacionario donde producción y disipación (difusión+reacción) se equilibran, mostrando un perfil espacial similar al de la fuente.

---

## Caso 5: Campo constante  
**Parámetros**  
- D = 0.05
- k = 0.01 
- f = 0  
- Vx = 1.0 (constante)  
- Vy = 0.5 (constante)  

![Animación 5: Campo constante](../results/animacion_caso5_fdm.gif)

**Conclusión**  
Con velocidades constantes la onda se desplaza uniformemente hacia la derecha y arriba. La difusión D=0.5 sigue aplanando la cresta, pero al no haber variación temporal o espacial en Vx/Vy la traslación es lineal y más predecible.

---

**Comentarios generales sobre el método de diferencias finitas**  
- El esquema θ (θ=0.5) garantiza estabilidad y segunda orden en tiempo cuando Δt y Δx cumplen la CFL.  
- El término de difusión suaviza las oscilaciones numéricas y modela correctamente la disipación.  
- La reacción –k u actúa como amortiguador global de la solución.  
- La fuente añade masa al sistema de manera controlada, permitiendo estudiar equilibrio producción–pérdida.

# Resultados del Método de Diferencias Finitas

**Condición inicial**  
Para todos los casos la condición inicial es el pulso gaussiano  
\[
u(x,y,0) = \exp\bigl(-50\,((x-0.5)^2 + (y-0.5)^2)\bigr)
\]  
discretizado con diferencias finitas P1 y evolucionado con el método $\theta$ ($\theta=0.5$, Crank–Nicolson).

---

## Caso 1: Sin difusión  
**Parámetros**  

\begin{itemize}
\item $D=0$
\item $k = 0.5$  
\item $f=0$
\item $V_{x} = 1.0 + 0.5 sin(2\pi t/Tfin) X  $
\item $V_{y} = 0.5 + 0.25 cos(2\pi t/Tfin) Y  $
\end{itemize}

![Animación 1: Sin difusión](../results/animacion1_fdm.gif)

**Conclusión**  
Al anular D, el término de difusión desaparece y la solución se transporta prácticamente sin cambio de forma: el pico de la gaussiana mantiene su altura mientras se desplaza, salvo pequeñas pérdidas en los bordes impuestas por las condiciones de contorno Dirichlet.

---

## Caso 2: Difusión moderada  
**Parámetros**  

\begin{itemize}
\item $D=0.5$
\item $k = 0.5$  
\item $f=0$
\item $V_{x} = 1.0 + 0.5 sin(2\pi t/Tfin) X  $
\item $V_{y} = 0.5 + 0.25 cos(2\pi t/Tfin) Y  $
\end{itemize}

![Animación 2: Difusión moderada](../results/animacion2_fdm.gif)

**Conclusión**  
Con $D=0.5$ la difusión suaviza rápidamente la curva: los gradientes se atenúan, la cresta se aplana y la anchura de la gaussiana aumenta, demostrando el papel disipativo del término Δu $\Delta u$ en el esquema de diferencias finitas.

---

## Caso 3: Reacción fuerte  
**Parámetros**  

\begin{itemize}
\item $D=0.5$
\item $k = 100$  
\item $f=0$
\item $V_{x} = 1.0 + 0.5 sin(2\pi t/Tfin) X  $
\item $V_{y} = 0.5 + 0.25 cos(2\pi t/Tfin) Y  $
\end{itemize}

![Animación 3: Reacción fuerte](../results/animacion3_fdm.gif)

**Conclusión**  
Al aumentar $k$ a $100$, el término de reacción domina y provoca una aniquilación rápida de la onda: la amplitud decae casi instantáneamente, mostrando el carácter fuertemente disipativo en la EDP.

---

## Caso 4: Fuente activada  
**Parámetros**  

\begin{itemize}
\item $D=0.5$
\item $k = 0.5$  
\item $f=(1 + t) sin(\pi x) sin(\pi y)  $
\item $V_{x} = 1.0 + 0.5 sin(2\pi t/Tfin) X  $
\item $V_{y} = 0.5 + 0.25 cos(2\pi t/Tfin) Y  $
\end{itemize}

![Animación 4: Fuente activada](../results/animacion4_fdm.gif)

**Conclusión**  
Con la fuente no homogénea, la solución crece en las zonas de inyección $(\sin\pi x\sin\pi y)$ y luego alcanza un estado pseudo–estacionario donde producción y disipación (difusión+reacción) se equilibran, mostrando un perfil espacial similar al de la fuente.

---

## Caso 5: Campo constante  
**Parámetros**  

\begin{itemize}
\item $D=0.5$
\item $k = 0.5$  
\item $f=(1 + t) sin(\pi x) sin(\pi y)  $
\item $V_{x} = 1.0 $
\item $V_{y} = 0.5 $
\end{itemize}

![Animación 5: Campo constante](../results/animacion5_fdm.gif)

**Conclusión**  
Con velocidades constantes la onda se desplaza uniformemente hacia la derecha y arriba. La difusión $D=0.5$ sigue aplanando la cresta, pero al no haber variación temporal o espacial en $V_{x}$/$V_{y}$ la traslación es lineal y más predecible.

---

**Comentarios generales sobre el método de diferencias finitas**  
- El esquema $\theta$ ($\theta=0.5$) garantiza estabilidad y segunda orden en tiempo cuando $\Delta t$ y $\Delta x$ cumplen la CFL.  
- El término de difusión suaviza las oscilaciones numéricas y modela correctamente la disipación.  
- La reacción $–k u$ actúa como amortiguador global de la solución.  
- La fuente añade masa al sistema de manera controlada, permitiendo estudiar equilibrio producción–pérdida.

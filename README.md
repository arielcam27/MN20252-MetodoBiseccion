# Método de la bisección
## Objetivo
Desarrollar una función en Python que encuentre la aproximación de una raíz de una función continua $f(x)$ dentro de un intervalo $[a, b]$ usando el **método de la bisección**.  

## Requisitos

1. **Función principal**  
   ```python
   def biseccion(f, a, b, tol=1e-6, max_iter=100):
       """
       Devuelve una aproximación de la raíz de f en [a, b].

       Parámetros
       ----------
       f        : callable
                  Función continua que recibe un float y devuelve un float.
       a, b     : float
                  Extremos del intervalo inicial (f(a)·f(b) < 0).
       tol      : float, opcional
                  Tolerancia absoluta deseada (criterio de parada).
       max_iter : int, opcional
                  Número máximo de iteraciones permitidas.

       Returns
       -------
       root : float
              Aproximación de la raíz.
       """
   ```


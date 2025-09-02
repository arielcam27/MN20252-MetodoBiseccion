# Método de la bisección
## Objetivo
Desarrollar una función en Python que encuentre la aproximación de una raíz de una función continua $f(x)$ dentro de un intervalo $[a, b]$ usando el **método de la bisección**.  

## Requisitos

1. **Función principal**  
   ```python
   def biseccion(f, a, b, tol, max_iter):
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

2. **Validaciones obligatorias**

- Verificar que $a < b$.
- Comprobar que $f(a)$ y $f(b)$ tengan signos opuestos $f(a) \times f(b) < 0$.
- Lanzar `ValueError` con mensaje descriptivo si alguna condición falla.

3. **Criterio de parada**

- El algoritmo termina cuando $|b-a| < tol$ o cuando se alcanza `max_iter`.
- En caso de alcanzar `max_iter` sin cumplir la tolerancia, lanzar `RuntimeError`.

4. **Documentación**

- ¿Docstring?
- Comentarios claros dentro del cuerpo de la función.

(Declaración uso de IA: Se usó Lumo de Proton como apoyo para la generación de esta plantilla. Revisé y adecué el contenido manualmente.)

from typing import Callable

def biseccion(
    f: Callable[[float], float],
    a: float,
    b: float,
    tol: float,
    max_iter: int,
) -> float:
    """
    Encuentra una raíz de la función `f` en el intervalo [a, b] usando
    el método de la bisección.

    Parameters
    ----------
    f : Callable[[float], float]
        Función continua cuyo signo cambia en el intervalo.
    a, b : float
        Extremos del intervalo inicial.
    tol : float, optional
        Tolerancia absoluta para el criterio de parada.
    max_iter : int, optional
        Número máximo de iteraciones permitidas.

    Returns
    -------
    float
        Aproximación de la raíz.

    Raises
    ------
    ValueError
        Si a >= b o si f(a) y f(b) no tienen signos opuestos.
    RuntimeError
        Si se supera `max_iter` sin alcanzar la tolerancia.
    """
    
    # Validaciones iniciales
  
    if a >= b:
        raise ValueError("El extremo izquierdo debe ser estrictamente menor que el derecho (a < b).")
    fa = f(a)
    fb = f(b)
    if fa == 0:
        return a
    if fb == 0:
        return b
    if fa * fb > 0:
        raise ValueError("f(a) y f(b) deben tener signos opuestos (producto negativo).")

    # Método de  la bisección
  
    for iteration in range(1, max_iter + 1):
        c = # TU CODIGO AQUI: punto medio
        fc = # TU CODIGO AQUI: evaluación de f en c

        # Criterio de parada basado en la longitud del intervalo
        if abs(b - a) < tol:
            return c

        # Actualizamos el sub‑intervalo que contiene la raíz
        if fa * fc < 0:          # la raíz está entre a y c
            b = c
            fb = fc
        else:                       # la raíz está entre c y b
            # TU CODIGO AQUI: sigue el patrón anterior

    # Si llegamos aquí, no alcanzamos la tolerancia requerida
    raise RuntimeError(
        f"No se alcanzó la tolerancia {tol} en {max_iter} iteraciones."
    )

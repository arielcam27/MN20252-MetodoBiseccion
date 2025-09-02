import json
import math
import pathlib

import pytest
from src.biseccion import biseccion


# Cargar los problemas definidos por el docente
PROBLEMS_PATH = pathlib.Path(__file__).parent.parent / "data" / "problems.json"
with open(PROBLEMS_PATH, "r") as f:
    PROBLEMS = json.load(f)


@pytest.mark.parametrize("key", PROBLEMS.keys())
def test_biseccion_problems(key):
    prob = PROBLEMS[key]

    # Convertir la cadena lambda a una función real
    func = eval(prob["func"], {"math": math, "__builtins__": {}})

    root = biseccion(
        f=func,
        a=prob["interval"][0],
        b=prob["interval"][1],
        tol=prob.get("tol", 1e-6),
        max_iter=200,
    )

    # Comparar con la raíz de referencia (tolerancia algo más estricta)
    assert math.isclose(root, prob["root_ref"], rel_tol=1e-7, abs_tol=1e-7)

from typing import Callable, Any
from operator import mod, eq
from functools import wraps


def compose(*funcs):
    def inner(args):
        state = args
        for func in funcs:
            state = func(state)
        return state
    return inner



def is_int(func: Callable) -> Callable:
    @wraps(func)
    def inner(val: Any) -> Any:
        return func(val) if isinstance(val, int) else val
    return inner


@is_int
def queijo(n: int) -> str:
    return 'queijo' if eq(mod(n,3), 0) else n


@is_int
def queijo_goiabada(n: int) -> str:
    return 'romeu e julieta' if eq(mod(n, 3), 0) and eq(mod(n, 5), 0) else n


@is_int
def goiabada(n: int) -> str:
    return 'goiabada' if eq(mod(n, 5), 0) else n


if __name__ == "app":
    romeu_julieta = compose(
        queijo_goiabada, 
        queijo, 
        goiabada)
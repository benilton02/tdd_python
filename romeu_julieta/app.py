from operator import mod, eq

def queijo(n: int) -> str:
    return 'queijo' if eq(mod(n,3), 0) else n


def queijo_goiabda(n: int) -> str:
    return 'romeu e julieta' if eq(mod(n, 3), 0) and eq(mod(n, 5), 0) else n


def goiabada(n: int) -> str:
    return 'goiabada' if eq(mod(n, 5), 0) else n


def romeu_julieta(val: int):
    if queijo_goiabda(val) == 'romeu e julieta':
        return 'romeu e julieta'

    if queijo(val) == 'queijo':
        return 'queijo'
    
    if goiabada(val) == 'goiabada':
        return 'goiabada'
    
    
'''
Tenho que fazer um código em que o OUTPUT seja o primeiro número
inteiro positivo faltante em uma sequencia

Por exemplo, na seguinte lista, o output seria o valor 2
numeros = [1, 3, 10, -2, -14, 20]
'''
from typing import List


def app(values: List[int]):
    
    if sum(values) < 0:
        return 1
   
    value = values[-1] + 1
    return value
    
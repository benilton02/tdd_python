'''
Tenho que fazer um código em que o OUTPUT seja o primeiro número
inteiro positivo faltante em uma sequencia

Por exemplo, na seguinte lista, o output seria o valor 2
numeros = [1, 3, 10, -2, -14, 20]
'''
from typing import List


def app(values: List[int]):
    
    if sum(values) <= 0:
        return 1
   
    if not values:
        return 1
    
    else:
        filtered_values = list(filter(lambda value: value > 0, sorted(values)))
        r = range(filtered_values[0], filtered_values[-1])
        
        for R, value in zip(r, filtered_values):
            if R != value:
                return R
        
        return filtered_values[-1] + 1

    
    
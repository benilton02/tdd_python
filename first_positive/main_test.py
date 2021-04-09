
'''
Casos de testes: 

A -> existem n numeros positivos
B -> não exitem numeros positivos, então retorna 1
c -> lista vazia, então retorna 1
D -> não existe numeros faltantes, então retorna o ULTIMO + 1
E -> lista com numeros inteiros não ordenados
'''


from unittest import TestCase, main
from app import app

class TestApp(TestCase):
    
    def test_a(self):
        esperado = 7
        resultado = app([1, 2, 3, 4, 5, 6])
        self.assertEqual(esperado, resultado)
        

if __name__ == "__main__":
    main()
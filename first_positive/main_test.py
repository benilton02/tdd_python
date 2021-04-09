
'''
Casos de testes: 

[ok] A -> existem n numeros positivos não ordenados
[ok] B -> não exitem numeros positivos, então retorna 1
[ok] c -> lista vazia, então retorna 1
[ok] D -> lista com numeros inteiros não ordenados
'''


from unittest import TestCase, main
from app import app

class TestApp(TestCase):
    
    def test_a(self):
        esperado = 7
        resultado = app([1, 2, 3, 4, 6, 5])
        self.assertEqual(esperado, resultado)

    def test_b(self):
        esperado = 1
        resultado = app([-1, 0])
        self.assertEqual(esperado, resultado)

    def test_c(self):
        esperado = 1
        resultado = app([])
        self.assertEqual(esperado, resultado)
    
    def test_d(self):
        esperado = 2
        resultado = app([1, 3, 10, -2, -14, 20])
        self.assertEqual(esperado, resultado)

if __name__ == "__main__":
    main()
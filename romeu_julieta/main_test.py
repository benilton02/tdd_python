"""
Romeu e Julieta

Entrada:
Uma entrada de valores interos

Saída
Se for multiplo de 3, então Queijo
Se for multiplo de 5, então Goiabada
se for multiplo de 3 e 5, então Romeu e Julieta

"""

from app import romeu_julieta
from unittest import(
    TestCase,
    main
)


class TestRomeuEJulita(TestCase):
   
    def teste_rej_deve_retornar_queijo_quando_input_for_multiplo_de_3(self):
        valores_entrada = [3, 6, 9]
        valor_esperado = "queijo"
        for valor_testado in valores_entrada:
            with self.subTest(valor_testado):
                self.assertEqual(romeu_julieta(valor_testado), valor_esperado)

    
    def teste_rej_deve_retornar_goiabada_quando_input_for_multiplo_de_5(self):
        valores_entrada = [5, 10, 20]
        valor_esperado = "goiabada" 
        for valor_testado in valores_entrada:
            with self.subTest(valor_testado):          
                self.assertEqual(romeu_julieta(valor_testado), valor_esperado)

    
    def teste_rej_deve_retornar_romeu_e_julieta_quando_input_for_15(self):
        valores_entrada = [15, 30, 60]
        valor_esperado = "romeu e julieta"
        for valor_testado in valores_entrada:
            with self.subTest(valor_testado):
                self.assertEqual(romeu_julieta(valor_testado), valor_esperado)
    

if __name__ == "__main__":
    main()
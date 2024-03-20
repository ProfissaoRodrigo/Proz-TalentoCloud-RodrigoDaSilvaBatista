Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> #Projeto Calculadora
... 
... def calculadora(valor1, valor2, operacao):
...     if operacao == 1:
...         return valor1 + valor2
...     elif operacao == 2:
...         return valor1 - valor2
...     if operacao == 3:
...         return valor1 * valor2
...     elif operacao == 4:
...         return valor1 / valor2
...     else:
...         return 0
... 
... resultado = calculadora (3, 8, 2)

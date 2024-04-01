Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> #Calculadora Infinita
... 
... print("Calculadora Infinita")
... 
... def soma(a,b):
...   return(a+b)
... def sub(a,b):
...   return(a-b)
... def mult(a,b):
...   return(a*b)
... def div(a,b):
...   return(a/b)
... 
... opcao = 1
... print("0. Sair")
... print("1. Somar")
... print("2. Subtrair")
... print("3. Multiplicação")
... print("4. Divisão ")
... 
... while opcao:
...   opcao = int(input("Escolha uma das opções acima. "))
...   
...   if opcao == 0:
...     print("Saindo")
...     break
... 
...   if opcao > 4:
...     print("Escolha uma opção válida!")
...     continue;
...   else:
...     num1=float(input("Primeiro numero: \n"))
...     num2=float(input("Segundo numero: \n"))
...     if opcao == 1:
...       print(num1,"+",num2,"é igual a: ",soma(num1,num2))
...     elif opcao == 2:
      print(num1,"-",num2,"é igual a: ",sub(num1,num2))
    elif opcao == 3:
      print(num1,"*",num2,"é igual a: ",mult(num1,num2))
    elif opcao == 4:
      print(num1,"/",num2,"é igual a: ",div(num1,num2))

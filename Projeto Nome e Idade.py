#Projeto Nome e Idade

#Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
#A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).
#Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

print("Digite seu nome completo:")

nome = input()

executar = True

while (executar == True):
  print("Digite seu ano de nascimento:")
  try:
    AnoDeNascimento = int(input())
    if (AnoDeNascimento < 1922 or AnoDeNascimento > 2022):
      print ("O ano deve estar entre 1922 e 2021")
    else:
        idade = 2022 - AnoDeNascimento
        print("O usuário", nome, "completou ou completará", idade, "anos de idade em 2022!")
        executar = False
  except:
        print("Campo vazio ou incorreto. O ano deve ser digitado em números!")

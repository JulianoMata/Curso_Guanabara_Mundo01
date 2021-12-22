"""Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
venceu ou perdeu. """


numero = float(input("Digite um número: "))
num = numero.random(1, 5)
if numero == num:
    print(f"O número é {numero} ")
else:
    print("Tente outra vez!!!")


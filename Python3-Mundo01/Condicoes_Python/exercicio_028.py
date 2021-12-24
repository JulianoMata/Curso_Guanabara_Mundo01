"""Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
venceu ou perdeu. """

from random import randint  # importa o metodo randint da biblioteca random para escolha aleatoria do numero
from time import sleep  # importa o metodo sleep da biblioteca time para determinar tempo de espera


computador = randint(0, 5)  # faz o computador "pensar"
print("-=-" * 20)
print("Vou pensar em um numero entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)

jogador = int(input("Pensei em qual numero? "))  # Jogador tenta adivinhar
print("PROCESSANDO...")
sleep(3)
if jogador == computador:
    print(f"O número é {computador} e você acertou!!")
else:
    print(f"Tente outra vez!!! O numero era {computador} e você digitou {jogador}")

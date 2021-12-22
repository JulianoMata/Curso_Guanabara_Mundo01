#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

#PRIMEIRO MODO
import math
# #.radians converte angulo para radianos
# angulo = float(input("Digite o ângulo que deseja: "))
# seno = math.sin(math.radians(angulo))
# cosseno = math.cos(math.radians(angulo))
# tangente = math.tan(math.radians(angulo))
# print(f"O ângulo de {angulo} tem o SENO de {seno :.2f}")
# print(f"O ângulo de {angulo} tem COSSENO de {cosseno :.2f}")
# print(f"O ângulo de {angulo} tem TANGENTE de {tangente :.2f}")


#SEGUNDO MODO
from math import radians, sin, cos, tan
angulo = float(input("Digite o ângulo que deseja: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f"O ângulo {angulo} tem SENO de {seno :.2f}")
print(f"O ângulo {angulo} tem COSSENO de {cosseno :.2f}")
print(f"O ângulo de {angulo} tem TANGENTE de {tangente :.2f}")

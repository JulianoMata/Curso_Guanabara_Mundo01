# Crie um programa que leia um número inteiro e mostre na tela se é par ou impar.

numero = int(input("Digite um número: "))
resultado = numero % 2   # resto da divisao por "2"
if resultado == 0:
    print("Número é 'Par'")
else:
    print("Número 'Ímpar'")

"""Desenvolva um programa que leia o comprimento de três restas e diga ao
usuário se elas podem ou não formar um triângulo"""

print("-=" * 20)
print("Analisador de triângulos")
print("-=" * 20)
lado1 = float(input("Digite um número: "))
lado2 = float(input("Digite segundo número: "))
lado3 = float(input("Digite terceiro número "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Os lados acima PODEM formar um triângulo!")
else:
    print("Os lados acima NÃO PODEM formar um triângulo!")




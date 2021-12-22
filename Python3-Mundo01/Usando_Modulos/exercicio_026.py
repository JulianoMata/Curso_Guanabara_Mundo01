# Faça um programa que leia uma frase pelo teclado e mostre:
# Qtas vezes aparece a letra "A".
# Em que posição ela parece pela primeira vez
# Em que posição ela aparece pela última vez

frase = str(input("Digite uma frase: ")).strip().upper()
print(f"A frase tem a letra A {frase.count('A')} vezes")
print(f"A letra aparece pela primeira vez {frase.find('A') + 1}")
print(f"A letra aparece pela última vez {frase.rfind('A') + 1}")
# print(frase.rfind("A"))


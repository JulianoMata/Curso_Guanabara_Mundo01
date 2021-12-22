# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas letras maiúsculas;
# O nome com todas letras minusculas;
# Quantas letras ao todo(sem considerar espaços)
# Quantas letras tem o primeiro nome


nome = str(input("Digite seu nome completo: ")).strip()
print(f"Seu nome em letra maiúscula é: {nome.upper()}")
print(f"Seu nome em letra minúscula é: {nome.lower()}")
print(f"Seu nome com iniciais maiúsculas é: {nome.title()}")

print(f"Seu nome tem {(len(nome) - nome.count(' '))} letras")
print(f"O primeiro nome tem {nome.find(' ')} letras")
# segundo modo
dividido = nome.split()
print(f"Seu primeiro nome é {dividido[0]} e tem {len(dividido[0])} letras")




# FATIAMENTO DE STRINGS
#
# frase = "Curso em Video Python"
# print(frase[9::3])
# print(len(frase))  # quantas letras na frases
# print(frase.count("o"))  # quantas vezes o "o" aparece
# print(frase.count("o", 0, 14))  # qtas vezes "o" na frase ate a posição 13
# print(frase.find("deo"))  # posição onde começa "deo"
# print(frase.find("Android"))  # retorna valor "-1" pq nao existe
# frase = frase.replace("Python", "Android")  # "strings" são imutáveis. Teria q alterar a variável frase
# print("Curso" in frase)  # retorna verdadeiro pq existe na frase
# print(frase.replace(" ", "-"))  # substitui na string de forma secundária
# print(frase.upper())  # maiúsculo
# print(frase.lower())  # minusculo
# print(frase.capitalize())  # Primeira letra da frase maiuscula
# print(frase.title())  # Primeira letra de cada palavra em maiuscula
# dividido = frase.split()  # separa a frase em uma lista de palavras
# print(dividido)  # printa a lista com as palavras divididas
# print(dividido[2][3])  # printa a letra posição "3" da palavra na posição "1"
#
# frase2 = "   Aprenda Python  "
# print(frase2.strip())  # remove os espaços antes e no final da frase
# print(frase2.rstrip())  # remove os espaços no final da frase
# print(frase2.lstrip())  # remove os espaços no início da frase
# print(len(frase2))
#
# print(frase.split())  # Cria uma divisão da frase conforme os espaços em uma lista, cada palavra
# tem seu proprio indice.
# print("-".join(frase))  # une as "strings" da frase com separação por "-", podendo usar qq caracter
# print("""Escrever um texto como um menu por exemplo é só colocar dentro de aspas triplas""")






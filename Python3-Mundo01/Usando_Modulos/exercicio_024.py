# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input("Digite o nome da cidade: ")).strip()
print(f"O nome da cidade começa com: {cidade}")
print(cidade[:5].upper() == "SANTO")

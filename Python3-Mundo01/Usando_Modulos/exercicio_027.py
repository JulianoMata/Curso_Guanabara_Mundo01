# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente.
# Ex: Ana Maria de Souza
# primeiro = Ana
# Último = Souza

nome = str(input("Digite o nome completo: ")).strip()

dividido = nome.split()
print(f"Prazer em te conhecer: {nome}")
print(f"Seu primeiro nome é {dividido[0]} e o último nome é {dividido[len(dividido) - 1]}")



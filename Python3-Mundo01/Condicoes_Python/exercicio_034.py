"""Escreva um programa que pergunte o salário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00 calcule aumento de 10%
Para os inferiores ou iguais o aumento é de 15%"""

salario = float(input("Digite o salario atual: "))
if salario <= 1250:
    print(f"Seu salário passou de R${salario} para R${salario + (salario * 0.15):.2f}")
else:
    print(f"Seu salário passou de R${salario} para R${salario + (salario * 0.10):.2f}")


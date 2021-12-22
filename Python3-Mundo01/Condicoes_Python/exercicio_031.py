""" Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0.50
por km para viagens de até 200 km e R$0.45 para viagens mais longas.

"""

distancia = float(input("Qual a distância da viagem? "))
valor1 = 0.50
valor2 = 0.45
if distancia <= 200:
    print(f"O valor da viagem foi {distancia * valor1 :.2f}")
else:
    print(f"O valor da viagem foi {distancia * valor2 :.2f}")





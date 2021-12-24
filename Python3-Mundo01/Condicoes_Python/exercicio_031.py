""" Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0.50
por km para viagens de até 200 km e R$0.45 para viagens mais longas.

"""

distancia = float(input("Qual a distância da viagem? "))
valor1 = 0.50
valor2 = 0.45
if distancia <= 200:
    print(f"O valor da viagem foi R${distancia * valor1 :.2f}")
else:
    print(f"O valor da viagem foi R${distancia * valor2 :.2f}")


# outra maneira

distancia = float(input("Qual a distância da sua viagem? "))
print(f"Você está prestes a começar uma viagem de {distancia}km")
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print(f"O preço da sua viagem será de R${preco:.2f}")


#  outra maneira

distancia = float(input("Qual a distância da sua viagem? "))
print(f"Você está prestes a começar uma viagem de {distancia}km")
preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print(f"O preço da sua viagem será de R${preco:.2f}")


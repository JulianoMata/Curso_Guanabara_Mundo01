""" Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""
# velocidadeMaxima = 80
# velocidadeAtual = float(input("Qual a velocidade? "))
# if velocidadeAtual <= velocidadeMaxima:
#     print("Tenha um bom dia, velocidade controlada!!!")
# else:
#     print("Você foi multado no valor de R$", (velocidadeAtual - velocidadeMaxima) * 7)


velocidade = int(input("Qual velocidade do atual do carro? "))
if velocidade > 80:
    print("Você foi multado, excedeu o limite de velocidade 80Km/h.")
    multa = (velocidade - 80) * 7
    print(f"Você deve pagar uma multa de R${multa:.2f}")
else:
    print("Tenha um bom dia!!! Direção preventiva")

# exemplo do guanabara sem o else da um erro, imprime de qq jeito a ultima msg

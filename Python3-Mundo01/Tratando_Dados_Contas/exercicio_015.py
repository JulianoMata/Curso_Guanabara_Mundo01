# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R0,15 por km rodado. 

quilometros = float(input("Digite a quantidade de km: "))
dias = int(input("Digite a quantidade de dias: "))
custo = (dias * 60) + (quilometros * 0.15)
print("A quantidade de quilometros percorredos foi {}km em {} dias ao valor total de R${:.2f}".format(quilometros, dias, custo))
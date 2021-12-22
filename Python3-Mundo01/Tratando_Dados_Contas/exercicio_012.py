# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 8% de desconto.


preco = float(input("Digite valor do produto: R$"))
novo_preco = preco - preco* 5 / 100
print("O valor do produto é R${:. 2f} e seu novo preço é R${;. 2f}".format( preco, novo_preco))
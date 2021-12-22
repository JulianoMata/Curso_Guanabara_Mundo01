# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere US$1,00 = R$5,68 (data 05/12/2021)
#testar euro = 6,41, libra esterlina= 7,53(Reino Unido), lene ou yuan = 0,89(chinesa)

real = float(input("Qto dinheiro você tem na carteira? R$"))
dolar = float(input("Qual valor dolar? "))
libra = float(input("Qual valor da libra esterlina? "))
iene = float(input("Qual o valor do iene japones? "))


dolar = real / dolar
libra = real / libra
iene = real / iene

print("Com R$ {:.2f} você pode comprar US${:.2f} ou £{:.2f} ou ¥{:.2f}".format(real, dolar, libra, iene))

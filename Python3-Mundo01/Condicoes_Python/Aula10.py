tempo = int(input("Quantos anos tem seu carro? "))
if tempo <= 3:
    print("Carro novo")
elif 3 < tempo < 10:
    print("Carro Velho")
else:
    print("Carro Muito Velho")
print("-- FIM --")

#  OUTRA MANEIRA
# tempo = int(input("Quantos anos tem seu carro?"))
# print("Carro novo" if tempo <= 3 else "carro muito velho")
# print("-- FIM --")


# outro exemplo

nome = str(input("Qual seu nome? ").upper().strip())
if nome == "JULIANO":
    print("Que lindo nome!!!")
else:
    pass
print(f"Bom dia, {nome}!!!")


# outro exemplo

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
media = (n1 + n2) / 2
print(f"Sua média foi {media:.2f}")
if media < 6.0:
    print("Sua media foi ruim!!!  Estude!!!")
elif 6.0 <= media <= 8.0:
    print("Sua média foi boa!!!")
else:
    print("Parabéns!!!")



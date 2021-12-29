# testando as cores em python

print("\033[7;31;44m teste de cores \033[m")
print("\033[1;31;45m teste de cores \033[m")
print("\033[1;32;44m teste de cores \033[m")
print("\033[1;33;40m teste de cores \033[m")
print("\033[7;34;42m teste de cores \033[m")
print("\033[7;30;41m teste de cores \033[m")

numero = int(input("Digite um número: "))
if numero >= 0:
    print("O número é \033[1;32;40m POSITIVO \033[m")
else:
    print("O número é \033[1;31;40m NEGATIVO \033[m")

###############################################################

nome = "Juliano"
print(f"Olá!!! Muito bom treino \033[4;34m{nome}\033[m!")

##############################################################

nome = "Guanabara"
cores = {"limpa": "\033[m",
         "azul": "\033[34m",
         "amarelo": "\033[33m",
         "pretoebranco": "\033[7;30m"}

print(f"Olá!! Boa noite, \033[4;34m{nome}\033[m!")





#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo. Calcule e mostre o comprimento da hipotenusa. 

#Metodo tradicional

# cateto_oposto = float(input("Digite o valor do cateto 01: "))
# cateto_adjacente = float(input("Digite o valor do cateto 02: "))
# hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
# print(f"O valor do primeiro cateto é {hipotenusa :.2f}")

#metodo dinamico

import math
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento cateto adjacente: "))
hi = math.hypot(co, ca)
print(f"O valor da hipotenusa é {hi :.2f} ")
           
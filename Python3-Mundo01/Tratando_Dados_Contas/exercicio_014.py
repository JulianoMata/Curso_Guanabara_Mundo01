# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit. 


# graus_celsius = float(input("Digite a temperatura em graus Celsius: "))
# fahrenheit = graus_celsius * 9 / 5 + 32
# print("A temperatura {}°C em fahrenheit é {}°F".format(graus_celsius, fahrenheit))


# converter fahrenheit para celsius

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
graus_celsius = (fahrenheit - 32) * 5/9
print("A temperatura {}°F em graus Celsius é {:.2f}°C".format(fahrenheit, graus_celsius))
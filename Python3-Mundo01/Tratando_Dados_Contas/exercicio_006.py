#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
num = int(input("Digite um número: \n"))
print(f"O dobro de {num} vale {num * 2}: ")
print(f"O triplo de {num} vale {num * 3}.\nA raiz quadrada de {num} é igual a {num **(1/2):.2f}.") # exibe 2 casas decimais e raiz quadrada atraves da exponenciação usando fração

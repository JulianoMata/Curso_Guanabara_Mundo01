#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. 


salario = float(input( "O salário atual é: R$"))
novo_salario = salario + salario * 15 / 100
print("O novo salário é: R${:.2f}".format(novo_salario))
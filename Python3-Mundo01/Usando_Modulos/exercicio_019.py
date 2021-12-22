#Um professor quer sortear um dos quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome do aluno e escrevendo na tela o nome do escolhido. 


from random import choice
#como não usamos toda biblioteca utilizamos o método "choice" para sortear um na lista

aluno01 = (input("Digite o nome primeiro aluno: "))
aluno02 = (input("Digite o nome do segundo aluno: "))
aluno03 = (input("digite o nome do terceiro aluno: "))
aluno04 = (input("Digite o nome do quarto aluno: "))
lista = [aluno01, aluno02, aluno03, aluno04]
escolhido = choice(lista)


print(f"O  aluno escolhido foi {escolhido}")




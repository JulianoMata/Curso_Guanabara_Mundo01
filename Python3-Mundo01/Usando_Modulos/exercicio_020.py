#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos de alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. 

from random import shuffle
# como não usa toda biblioteca importamos apenas o método "shuffle" para embaralhar os nomes

aluno01 = input("Digite o nome aluno 01: ")
aluno02 = input("Digite o nome aluno 02: ")
aluno03 = input("Digite o nome aluno 03: ")
aluno04 = input("Digite o nome aluno 04: ")
lista = [aluno01, aluno02, aluno03, aluno04]
shuffle(lista)
print(lista)

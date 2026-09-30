#Sorteando sequência aleatória
import random

a = str(input('Digite o nome do aluno: '))
b = str(input('Digite o nome do aluno: '))
c = str(input('Digite o nome do aluno: '))
d = str(input('Digite o nome do aluno: '))

lista = [a, b, c, d]
random.shuffle(lista)

print(lista)
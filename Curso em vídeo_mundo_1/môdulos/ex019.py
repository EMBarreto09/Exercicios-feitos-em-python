#Sorteando um item aleatório
import random

a = input('Qual o primeiro aluno: ')
b = input('Qual o segundo aluno: ')
c = input('Qual o terceiro aluno: ')
d = input('Qual o quarto aluno: ')

e = [a, b, c, d]
i = random.choice(e)

print(i)
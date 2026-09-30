#Jogo de advinhação v2

from random import randint

computador = randint(0, 10)
jogador = ""

print('Olá sou seu computador')
print('tente advinhar qual número estou pensando de 0 a 10')

while jogador != computador:
    jogador = int(input('Digite um número de 0 a 10: '))
    if computador > jogador:
        print('mais')
        print('Tente novamente')
    elif computador < jogador:
        print('menos')
        print('Tente novamente')
    elif computador == jogador:
        print('Parabéns')
        print('Você acertou!!!')
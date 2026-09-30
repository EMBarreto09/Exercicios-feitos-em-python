#JOKENPÔ aprimorado
from time import sleep
from random import choice

escolha2 = 's'

jogador = 0
comp = 0

lista = ['PEDRA', 'PAPEL', 'TESOURA']

print('=================')
print('JOKENPÔ')
print('=================')
print('O JOGO ACABA COM QUEM FIZER 3 PONTOS')

nome = str(input('Qual o seu nome: '))

while escolha2 == 's':

    computador = choice(lista)
    
    print("""[1] - PEDRA
[2] - PAPEL
[3] - TESOURA""")

    escolha = input('<<<Escolha uma das opções acima>>> ')
    print("")

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')
    print("")
    if escolha == '1':
        print(f'{nome} escolheu PEDRA')
        print(f'COMPUTADOR escolheu {computador}')
        if escolha == '1' and computador == 'TESOURA':
            print(f'VENCE {nome}')
            jogador +=1
        elif escolha == '1' and computador == 'PAPEL':
            print('VENCE COMPUTADOR')
            comp +=1
        else:
            print('EMPATE')
    elif escolha == '2':
        print(f'{nome} escolheu PAPEL')
        print(f'COMPUTADOR escolheu {computador}')
        if escolha == '2' and computador == 'PEDRA':
            print(f'VENCE {nome}')
            jogador +=1
        elif escolha == '2' and computador == 'TESOURA':
            print('VENCE COMPUTADOR')
            comp +=1
        else:
            print('EMPATE')
    elif escolha == '3':
        print(f'{nome} escolheu TESOURA')
        print(f'COMPUTADOR escolheu {computador}')
        if escolha == '3' and computador == 'PAPEL':
            print(f'VENCE {nome}')
            jogador +=1
        elif escolha == '3' and computador == 'PEDRA':
            print('VENCE COMPUTADOR')
            comp +=1
        else:
            print('EMPATE')
    print("")
    print('========PLACAR========')
    print(f'{nome} {jogador} x {comp} COMPUTADOR')
    print("")

    if jogador == 3:
        print(f'VITÓRIA DO {nome}!!!')
        break
    elif comp == 3:
        print('VITÓRIA DO COMPUTADOR!!!')
        break
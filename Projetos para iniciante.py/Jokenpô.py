import random

print('------------------------')
print('Pedra, Papel, Tesoura')
print('------------------------')

usuario = input('Escolha algumas das três opções: ')
print(f'Você escolheu {usuario}')

lista = ['Pedra', 'Papel', 'Tesoura']

comp = random.choice(lista)
print(f'Eu escolho {comp}')
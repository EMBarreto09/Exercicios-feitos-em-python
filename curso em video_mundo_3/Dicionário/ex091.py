#Jogo de dados

from random import randint
from time import sleep
from operator import itemgetter

dado = {'jogador1': randint(1, 6), 
'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 
'jogador4': randint(1, 6)}

ranking = {}

for k, v in dado.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)

print()

print('Ranking do Jogadores')
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)

for r in ranking:
    print(r)

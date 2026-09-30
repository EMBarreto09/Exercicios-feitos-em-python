#Cadastro jogador

cont1 = 0
cont = 1
jogador = {}
lista = []

jogador['nome'] = str(input('nome do jogador: '))
partidas = int(input('Quantas partidas ele jogou: '))

if partidas > 0:
    for p in range(partidas):
        lista.append(int(input(f'   Quantos gols ele fez no {cont} jogo: ')))
        cont += 1

jogador['gols'] = lista
jogador['total'] = sum(lista)

print('='*20, 'MODELO 1', '='*20)
print(jogador)

print('='*20, 'MODELO 2', '='*20)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('='*20, 'MODELO 3', '='*20)
print(f'O jogador {jogador['nome']} jogou {partidas} partidas')

for g in range(partidas):
    print(f'=> Na partida {cont1}, {jogador['nome']} marcou {lista[cont1]} gols')
    cont1 += 1
print(f'Um total de {sum(lista)} gols')


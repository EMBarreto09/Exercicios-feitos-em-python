#Aprimoramento do cadastro de futebol

lista = []
jogador = {}
cont = 1
gols = []

while True:
    jogador.clear()
    gols.clear()

    print('-'* 10, 'CADASTRO DE JOGADORES', '-'* 10)
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input('Quantas partidas ele jogou: '))

    if jogador['partidas'] > 0:
        while cont <= jogador['partidas']:
            gols.append(int(input(f'  Quantos gols o jogador fez na {cont}ª partida: ')))  
            cont += 1  

    if cont > jogador['partidas']:
        cont = 1

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    lista.append(jogador.copy()) 

    escolha = str(input('Deseja continuar [s/n]: ')).strip().lower()[0]

    while escolha not in 'ns':
        escolha = str(input('ERRO!, digite s ou n: ')).strip().lower()[0]
    if escolha == 'n':
        break
    else:
        continue

print('cod', end=' ')
for c in jogador.keys():
    print(f'{c:^15}', end=' ')
    
print()

for k, v in enumerate(lista):
    print(f'{k:^5}', end=' ')
    for d in v.values():
        print(f'{str(d):^15}', end=' ')
    print()

while True:
    busca = int(input('Qual jogador você quer ver o aproveitamento [999 para encerrar]: '))

    if busca == 999:
        break
    if busca >= len(lista):
        print("Erro, não temos esse código")
    else: 
        print(f'Levantamento do jogador {lista[busca]['nome']}'),
        for i, g in enumerate(lista[busca]['gols']):
            print(f'    No jogo {i+1} ele fez {g} gols')
        
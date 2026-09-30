#Tabela brasileirão

brasileirao = ('Palmeiras', 'Flamengo', 'Athletico-PR', 'Fluminense',
'Bragantino', 'Bahia', 'Botafogo', 'Atlético-MG', 'Corinthians', 'Coritiba',
'Cruzeiro', 'São Paulo', 'EC Vitória', 'Santos', 'Grêmio', 'internacional',
'vasco da gama', 'Remo', 'Mirassol', 'chapecoense')

print('='*30)
print(f'Os primeiros 5 colocados são: {brasileirao[:5]}')
print('='*30)
print(f'Os últimos 4 colocados são: {brasileirao[-4:]}')
print('='*30)
print(f'Está é a lista em ordem alfabética: {sorted(brasileirao)}')
print('='*30)
print(f'O time Chapecoense está na {brasileirao.index('chapecoense') + 1}ª posição')
print('='*30)
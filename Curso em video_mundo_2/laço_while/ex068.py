#Par ou ímpar
from random import randint

computador = randint(1, 10)

jogador = 0
comput = 0

print('-'*30)
print('=====JOGO DO PAR OU ÍMPAR=====')
print('-'*30)

while True:
    
    usuario = int(input('Digite um número: '))
    par_impar = str(input('par ou Ímpar: ')).strip().lower()[0]
    if par_impar == 'p':
        soma_usuario = usuario + computador
        if soma_usuario %2 == 0:
            print(f'A soma entre {usuario} e {computador} resulta em {soma_usuario}')
            print('Vitória JOGADOR')
            jogador += 1
        else:
            print(f'A soma entre {usuario} e {computador} resulta em {soma_usuario}')
            print('Vitória COMPUTADOR')
            comput += 1
    if par_impar == 'i':
        soma_usuario = usuario + computador
        if soma_usuario %3 == 0:
            print(f'A soma entre {usuario} e {computador} resulta em {soma_usuario}')
            print('Vitória JOGADOR')
            jogador += 1
        else:
            print(f'A soma entre {usuario} e {computador} resulta em {soma_usuario}')
            print('Vitória COMPUTADOR')
            comput += 1
    if comput == 1:
        print(f'O JOGADOR venceu {jogador} vezes do COMPUTADOR')
        break
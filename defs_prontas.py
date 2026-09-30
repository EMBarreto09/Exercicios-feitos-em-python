#Como Usar?
#No topo do código colocar (from defs_prontas import (e a def desejada) ou)
#colocar import defs_prontas e depois importar no comando. Ex: defs_prontas.factorial  <- mais recomendada


#Calculo de fatorial com um show (mostra ou não a sequência do produto)
def factorial(num, show):
    f = 1
    if show == True:
        for c in range(num, 0, -1):
            print(c, end=' ')
            print('x' if c > 1 else '->', end=' ')
            f *= c
        print(f) 
    else:
        for c in range(num, 0, -1):
            f *= c
        print(f)  

#Calcula a área de um terreno
def terreno(l, c):
    area = l * c
    print(f'A área das dimensões {l} x {c} é igual a {area:.2f}')

#Texto do tamanho da palavra
def texto(txt):
    print('-' * (len(txt) + 4))
    print(f'  {txt}')
    print('-' * (len(txt) + 4))

#Contador
def contador(a1, an, r):
    from time import sleep
    print('=' * 30)
    print(f'Contagem de {a1} até {an} de {r} em {r}')
    print('=' * 30)
    n = a1
    if n < an:
        while n <= an:   
            print(n, end=' ', flush=True)
            sleep(0.1)
            n += r
    else:
        while n >= an:
            print(n, end=' ', flush=True)
            sleep(0.1)
            n -= r

#Maior número
def maior(*num):
    from time import sleep
    print('Analisando os números digitados...')

    maior = 0
    cont = 0

    for n in num:
        print(n, end=' ', flush=True)
        sleep(0.2)
        if cont == 0:
            maior = n
        if n > maior:
            maior = n
        cont += 1
    print(f'Ao todo foram {len(num)} números digitados')
    print(f'E o maior deles é o número {maior}')

#Sorteia números aleatórios
def sortear():
    from time import sleep
    for n in range(10):
        num.append(randint(1, 100))
    print(f'Valores sorteados...')
    for v in num:
        print(v, end=' ', flush=True)
        sleep(0.2)

#Soma os números pares
def somar_par():
    par = 0
    for c in num:
        if c % 2 == 0:
            par += c
    print(f'\nA soma dos pares são {par}')

#Verificação de voto
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos. Não pode votar'
    elif idade < 18 and idade > 15 or idade > 69:
        return f'Com {idade} anos. O voto é opcional'
    else:
        return f'Com {idade} anos. O voto é obrigatório'

#Ler se o número é int ou str
def leiaint(n):
    if n.isnumeric():
        print(f'Você digitou o número {n}')
    else:
        while n.isalnum:
            print(f'\033[1;31mERRO. ISSO NÃO É UM NÚMERO\033[m')
            num = input('Digite um número: ')
            if num.isnumeric():
                print(f'Você digitou o número {num}')
                break

#Verificador de notas
def notas(*num, sit=True):

    geral['total'] = len(num)

    media = 0
    geral['maior'] = num[0]
    geral['menor'] = num[0]

    for i in num:
        if i > geral['maior']:
            geral['maior'] = i
    
    for c in num:
        if c < geral['menor']:
            geral['menor'] = c

    for m in num:
        media += m
        geral['media_total'] = media / len(num)
   
    if sit == True:
        if geral['media_total'] < 5:
            geral['situação'] = 'Ruim'
        elif 6 > geral['media_total'] < 7:
            geral['situação'] = 'Mediana'
        else:
            geral['situação'] = 'Ótimo'
    
    print(geral)

#Sistema de ajuda (HELP)
def ajuda():
    while True:
        print('\033[1;32;42m=-\033[m'* 15)
        print('\033[1;32;42m<<<SISTEMA DE AJUDA PyHELP>>>>\033[m')
        print('\033[1;32;42m=-\033[m'* 15)
        print('\033[m')

        sos = str(input('Função ou Biblioteca: ')).strip()

        print()

        if sos == 'fim':
            break
        else:
            print('\033[1;35;45m=-'* 20)
            print(f'\033[1;45m<<Acessando o manual do comando {sos}>>>')
            print('\033[1;35;45m=-\033[1;97m'* 20)
            help(sos)

#Dobro de um número
def dobro(preço):
    dob = preço * 2
    return dob

#Metade de um número
def metade(preço):
    pre = preço / 2
    return pre

#Aumentar um número em 10%
def aumentar(preço, taxa=10):
    aum = preço + (preço * taxa/100)
    return aum

#Diminuir um número em 13%
def diminuir(preço, taxa=13):
    dim = preço - (preço  * taxa/100)
    return dim
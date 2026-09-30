#Menu de opções

escolha = " "

print('==========MENU DE OPÇÕES==========')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

while escolha != '5':
    print("")
    print("""[1] = Somar
[2] = Multiplicar
[3] = maior
[4] = novos números
[5] = sair do programa""")
    escolha = str(input('Escolha uma das opções acima>>> '))
    print("")
    if escolha == '1':
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} é igual a {soma}')
    elif escolha == '2':
        multiplicacao = n1 * n2
        print(f'O resultado de {n1} vezes {n2} é igual a {multiplicacao}')
    elif escolha == '3':
        if n1 > n2:
            print(f'entre {n1} e {n2} o {n1} é o maior')
        else:
            print(f'entre {n1} e {n2} o {n2} é o maior')
    elif escolha == '4':
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número'))
    elif escolha == '5':
        break

print('Fim do programa')

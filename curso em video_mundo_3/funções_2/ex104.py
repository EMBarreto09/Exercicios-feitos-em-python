#Validando dados

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

n = leiaint(input('Digite um número: '))
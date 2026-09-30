#Verificador de numero primo

total = 0

numero = int(input("Digite um número para ver se é primo: "))

for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end='')
        print(c, end=' ')
        print('\033[m', end='')
        total += 1
    else:
        print(c, end=' ')

print(f'\nO número {numero} foi divido {total} vezes')

if total == 2:
    print(f'O número {numero} é primo')
else:
    print(f'O número {numero} não é primo')
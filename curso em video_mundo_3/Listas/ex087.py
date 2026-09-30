#Mais sobre matriz

lista = [[[],[],[]],[[],[],[]],[[],[],[]]]

soma = 0
soma_c = 0
maior = 0

for l in range(0,3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('='*25)

for l in range(0, 3):
    if l != 0:
        print()
    for c in range(0, 3):
        print(f'[{lista[l][c]:^4}]', end=' ')
        if lista[l][c] % 2 == 0:
            soma += lista[l][c]
        if c == 2:
            soma_c += lista[l][c]
        if l == 1:
            maior = lista[l][c]
            if lista[l][c] > maior:
                maior = lista[l][c]
        
print(f'\nA soma de todos os pares são: {soma}')
print(f'A soma da terceira coluna é: {soma_c}')
print(f'O maior valor da segunda linha é: {maior}')
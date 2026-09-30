#Matriz

lista = [[[],[],[]],[[],[],[]],[[],[],[]]]

for l in range(0,3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('='*25)

for l in range(0, 3):
    if l != 0:
        print()
    for c in range(0, 3):
        print(f'[{lista[l][c]:^4}]', end=' ')
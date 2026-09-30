#lista de preços com tuplas

nome = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 
9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*25)
print('LISTAGEM DE PREÇOS')
print('-'*25)

for pos in range(0, len(nome)):
    if pos % 2 == 0:
        print(f'{nome[pos]:.<30}', end=' ')
    else:
        print(f'R${nome[pos]:>10}')

    
    
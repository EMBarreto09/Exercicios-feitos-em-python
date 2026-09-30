#Ordenar valores sem o sort

cont = 0
lista = []

for c in range(5):
    numero = int(input('Digite um número: '))
    if cont == 0:
        lista.append(numero)
        print(f'Número {numero} adicionado ao final da lista')
    if cont == 1:
        if numero > lista[0]:
            print(f'Número {numero} adicionado ao final da lista')
            lista.append(numero)
        else:
            print(f'Número {numero} adicionado na posição 0')
            lista.insert(0, numero)
    if cont == 2:
        if numero > lista[1]:
            print(f'Número {numero} adicionado ao final da lista')
            lista.append(numero)
        elif numero < lista[0]:
            print(f'Número {numero} adicionado ao final da lista')
            lista.insert(0, numero)
        elif numero < lista[1] and numero > lista[0]:
            print(f'Número {numero} adicionado a posição 1')
            lista.insert(1, numero)
    if cont == 3:
        if numero > lista[2]:
            print(f'Número {numero} adicionado ao final da lista')
            lista.append(numero)
        elif numero < lista[0]:
            print(f'Número {numero} adicionado ao final da lista')
            lista.insert(0, numero)
        elif numero < lista[1] and numero > lista[0]:
            print(f'Número {numero} adicionado a posição 1')
            lista.insert(1, numero)
        elif numero < lista[2] and numero > lista[0]:
            print(f'Número {numero} adicionado a posição 2')
            lista.insert(2, numero)
    if cont == 4:
        if numero > lista[3]:
            print(f'Número {numero} adicionado ao final da lista')
            lista.append(numero)
        elif numero < lista[0]:
            print(f'Número {numero} adicionado ao final da lista')
            lista.insert(0, numero)
        elif numero < lista[1] and numero > lista[0]:
            print(f'Número {numero} adicionado a posição 1')
            lista.insert(1, numero)
        elif numero < lista[2] and numero > lista[0]:
            print(f'Número {numero} adicionado a posição 2')
            lista.insert(2, numero)
        elif numero < lista[3] and numero > lista[0]:
            print(f'Número {numero} adicionado a posição 3')

    cont += 1
    
print('A ordem dos números digitados são')

for n in lista:
    print(n, end=' ')
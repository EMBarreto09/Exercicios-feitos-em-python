#Pares e Ímpares

lista = [[], []]
cont = 1

for i in range(7):
    n = int(input(f'Digite o {cont}º número: '))
    cont += 1

    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

print(f'Os números cadastrados pares são: {lista[0]}')
print(f'os números cadastrados ìmpares são: {lista[1]}')
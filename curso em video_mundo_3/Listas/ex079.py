#Valores únicos em uma lista

lista = []

while True:
    numero = int(input('Digite um número: '))
    if numero not in lista:
        lista.append(numero)
    else:
        print('Valor duplicado. Não irei adicionar')

    escolha = str(input('Quer continuar [s/n] > ')).lower().strip()[0]

    if escolha != 's':
        break

lista.sort()
print(lista)
#Dividindo a lista

lista = []
lista_par = []
lista_impar = []

while True:
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        lista.append(numero)
        lista_par.append(numero)
    else:
        lista.append(numero)
        lista_impar.append(numero)

    escolha = str(input('Deseja continuar [s/n]: ')).strip().lower()[0]

    if escolha != 's':
        break

print('Lista completa')
print('-'*10)
print(lista)
print('-'*10)
print('Lista dos pares')
print('-'*10)
print(lista_par)
print('-'*10)
print('Lista do impares')
print('-'*10)
print(lista_impar)
print('-'*10)
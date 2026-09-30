#Extração de dados da lista

lista = []

while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)

    escolha = str(input('Deseja continuar [s/n] > ')).strip().lower()[0]

    if escolha != 's':
        break

lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números')
print(f'A ordem decrescente desses numeros são {lista}')

if 5 in lista:
    print(f'O número 5 está na lista')
else:
    print('O número 5 não está na lista')
        
#Tratando números

numero = int(input('Digite um número > [999] para encerrar: '))

lista = []

while numero != 999:
    numero = int(input('Digite um número > [999] para encerrar: '))
    lista.append(numero)
    if numero == 999:
        print(f'Foram {len(lista)} números digitados')
        lista.remove(999)
        print(f'E a soma entre eles é {sum(lista)}')
        break
        
    
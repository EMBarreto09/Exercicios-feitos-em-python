#Tratando números

numero = int(input('Digite um número > [999] para encerrar: '))

soma = 0
contador = 0

while numero != 999:
    numero = int(input('Digite um número > [999] para encerrar: '))
    
    if numero == 999:
        break

    soma += numero
    contador += 1

print(f'Foram {contador} números digitados')
print(f'E a soma entre eles é {soma}')
        
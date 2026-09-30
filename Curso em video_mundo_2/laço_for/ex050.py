#Soma dos pares

soma_pares = 0
soma_numeros = 0

for c in range(6):
    numero = int(input('Digite um número: '))
    soma_numeros += 1
    if numero %2 == 0:
        soma_pares += numero

print(f'Foram digitados {soma_numeros} números')
print(f'A soma entre os pares digitados é de {soma_pares}')
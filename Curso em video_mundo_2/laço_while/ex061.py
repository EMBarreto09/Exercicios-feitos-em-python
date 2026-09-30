#PA

termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
primeiro = termo
contador = 1

while contador <= 10:
    print(primeiro, end=' > ')
    primeiro += razao
    contador += 1

print('Fim')
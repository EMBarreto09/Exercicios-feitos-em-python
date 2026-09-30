#Tabuada V2.0

numero = int(input('Digite um número para ver sua tabuada: '))

for c in range(1, 11):
    resultado = numero * c
    print(f'{numero} X {c} = {resultado}')

print('Fim')
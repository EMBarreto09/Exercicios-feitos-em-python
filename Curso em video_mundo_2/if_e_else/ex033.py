#Número maior e menor

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

maior = n1
menor = n1

if n2 < maior:
    print(f'O número {n2} é o menor')
elif n2 < menor:
    print(f'O número {n2} é o menor')
else:
    print(f'O número {n1} é o menor')

if n3 > maior:
    print(f'O número {n3} é o maior')
elif n3 > menor:
    print(f'O número {n3} é o maior') 
#Calcular preço da viagem

km = int(input('Digite a distância da sua viagem: '))

preco = km * 0.55
preco1 = km * 0.45

if km <= 200:
    print(f'{preco:.2f}')
else:
    print(f'{preco1:.2f}')

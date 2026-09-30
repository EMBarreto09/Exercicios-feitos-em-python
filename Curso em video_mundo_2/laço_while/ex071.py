#caixa eletrônico

valor = int(input('Digite um valor para sacar: '))

executando = True
valor50 = 0
valor20 = 0 
valor10 = 0
valor1 = 0

while executando:
    while valor >= 50:
        valor -= 50
        valor50 += 1
    while valor >= 20 and valor < 50:
        valor -= 20
        valor20 += 1
    while valor >= 10 and valor < 20:
        valor -= 10
        valor10 += 1
    while valor >= 1 and valor < 10:
        valor -= 1
        valor1 += 1
    executando = False

if valor50 != 0:
    print(f'Você retirou {valor50} notas de R$50')
if valor20 != 0:
    print(f'Você retirou {valor20} notas de R$20')
if valor10 != 0:
    print(f'Você retirou {valor10} notas de R$10')
if valor1 != 0:
    print(f'Você retirou {valor1} notas de R$1')
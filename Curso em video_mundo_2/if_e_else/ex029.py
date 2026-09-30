#Calculador de multa

velocidade = int(input('Digite em que velocidade você ultrapassou a via: '))

multa = (velocidade - 80) * 7

if velocidade > 80:
    print('Você foi multado!!!')
    print(f'O valor a ser pago irá ser de {multa} Reais')
else:
    print('Você não foi multado!')
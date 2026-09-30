#Calculo de carro alugado

km = float(input('Digite quantos km foram rodados: '))
dias = int(input('Digite quantos dias foi alugado: '))

km1 = km * 0.15
dias1 = dias * 60
total = km1 + dias1

print(f'O total do carro alugado a ser pago é um total de: R${total}')
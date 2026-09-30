#Tabuada v3.0
contador = 0
numero = int(input('Digite um número para ver sua tabuada ou um número negativo para encerrar: '))

while contador < 11:
    if numero > -1:
        resultado = numero * contador
        print(f'{numero} X {contador} = {resultado}')
        contador += 1
        if contador == 11:
            contador -= 10
            numero = int(input('Digite um número para ver sua tabuada ou um número negativo para encerrar: '))
    else:
        print('Fim')
        break
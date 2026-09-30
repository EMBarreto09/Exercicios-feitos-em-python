#Número por extenso
numeros = ('zero', 'um', 'dois','três', 'quatro', 'cinco')
executando = True

numero = int(input('Digite um número entre 0 a 5: '))

while executando:
    if numero >= 0 and numero <= 5:
        print(f'O número digitado foi o número {numeros[numero]}')
        executando = False
    else:
        numero = int(input('Tente novamente. Digite um número entre 0 a 5: '))
        
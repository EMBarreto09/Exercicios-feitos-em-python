import random

numero = random.randint(1,100)
escolha = ""
tentativa = 0
while escolha != numero:
    escolha = int(input('Digite um número de 1 até 100: '))
    if numero > escolha:
        print('O número é maior')
        tentativa += 1
    elif numero < escolha:
        print('O número é menor')
        tentativa += 1
    else:
        print('Acertou o número escolhido')
        tentativa += 1

print(f'Você precisou de {tentativa} tentativas para acertar!')
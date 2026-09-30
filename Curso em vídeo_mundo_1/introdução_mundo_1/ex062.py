termo = int(input('Termo: '))
razao = int(input('Razão: '))
primeiro = termo
contador = 1
segundo = contador
termo_2 = 1

while contador <= 10:
    print(primeiro, end=' > ')
    contador += 1
    primeiro += razao
    segundo += contador
    if contador > 10:
        print('Fim')
        while termo_2 != 0:
            termo_2 = int(input('Digite quantos termos você quer a mais: '))
            segundo = contador + termo_2
            while contador < segundo:
                print(primeiro, end=' > ')
                contador += 1
                primeiro += razao
                if contador == segundo:
                    print('Fim')
            

print('Fim')
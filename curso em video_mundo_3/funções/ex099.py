#Maior

from time import sleep

def maior(*num):
    print('Analisando os números digitados...')

    maior = 0
    cont = 0

    for n in num:
        print(n, end=' ', flush=True)
        sleep(0.2)
        if cont == 0:
            maior = n
        if n > maior:
            maior = n
        cont += 1
    print(f'Ao todo foram {len(num)} números digitados')
    print(f'E o maior deles é o número {maior}')

maior(3, 4, 5, 2, 3, 4, 1, 27, 47, 31, 67, 34)
maior(24, 56, 34, 68, 45, 234, 547, 65, 2352, 6856, 45, 436457)
maior(1, 2 ,3 ,4, 5, 6 ,7 ,8, 9, 10)
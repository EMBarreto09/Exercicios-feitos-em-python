#Contador

from time import sleep

def contador(a1, an, r):
    print('=' * 30)
    print(f'Contagem de {a1} até {an} de {r} em {r}')
    print('=' * 30)
    n = a1
    if n < an:
        while n <= an:   
            print(n, end=' ', flush=True)
            sleep(0.1)
            n += r
    else:
        while n >= an:
            print(n, end=' ', flush=True)
            sleep(0.1)
            n -= r
    
contador(1, 10, 1) 
print()
contador(10, 0, 2)    
print()

print('=' * 35)
print('Agora é a sua vez de escolher a sequência')
print('=' * 35)

a1 = int(input('Inicio: '))
an = int(input('Fim: '))
r = int(input('Passo: '))

contador(a1, an, r)
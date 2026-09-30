#Fatorial

def factorial(num, show):
    f = 1
    if show == True:
        for c in range(num, 0, -1):
            print(c, end=' ')
            print('x' if c > 1 else '->', end=' ')
            f *= c
        print(f) 
    else:
        for c in range(num, 0, -1):
            f *= c
        print(f)   
def lin():
    print('=-'*15)

fac = int(input('Qual número deseja calcular: '))

print(f'Calculando fatorial de {fac}...')

lin()
factorial(fac, show=True)
lin()
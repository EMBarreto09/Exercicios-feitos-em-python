#advinhe o número
import random

numero = random.randint(1,5)

usuario = int(input('Advinhe o número de 1 a 5: '))

if usuario == numero:
    print('\033[1;32;40mParabéns acertou\033[m')
else:
    print('\033[1;31;40merrou\033[m')
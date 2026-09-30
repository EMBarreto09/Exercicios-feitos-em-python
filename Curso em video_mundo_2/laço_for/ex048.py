#Caluclo impares

soma = 0
soma2 = 0

for c in range(1 , 501):
    if c %3 == 0 and c %2 != 0:
        soma2 += 1
        soma += c
print(f'Todos os números ìmpares e multiplos de 3 são ao todo {soma2}')
print(f'A soma é {soma}')
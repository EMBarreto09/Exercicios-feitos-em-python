#Analisando tuplas

valor9 = 0

valores = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))

for v in valores:
    if v == 9:
        valor9 += 1

print(f'Você digitou os valores {valores}')
print(f'O valor 9 aparece {valor9} vezes')

if 3 in valores:
    print(f'o valor 3 aparece na {valores.index(3) + 1}ª posição') 
else:
    print(f'Não foi digitado nenhum valor 3')

print(f'Os valores pares foram:', end=' ')

for v in valores:
    if v % 2 == 0:
        print(v, end=' ')
#Sequência de fibonacci
termo = int(input('Digite quantos termos você quer: '))

cont = 3
primeiro = 0
segundo = 1

print(primeiro, end=' > ')
print(segundo, end=' > ')

while cont <= termo:
    terceiro = primeiro + segundo
    print(terceiro, end=' > ')
    primeiro = segundo
    segundo = terceiro
    cont += 1

print('Fim')
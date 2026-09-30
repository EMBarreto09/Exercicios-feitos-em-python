#Maior e menor valor

lista = []
continuar = 's'

while continuar == 's':
    numero = int(input('Digite um número: '))
    lista.append(numero)
    continuar = str(input('Deseja continuar [s/n]: ')).lower()
    media = sum(lista) / len(lista)

print(f'você digitou {len(lista)} números')
print(f'Á média entre eles é de {media:.2f}')
print(f'O maior valor digitado é o {max(lista)} e o menor valor digitado é o {min(lista)}')
    
#Maior e menor

lista = []

for c in range(5):
    valor = int(input(f'Digite um valor para a posição {c}: '))
    lista.append(valor)

print(f'O maior número digitado é {max(lista)}')
print(f'O menor número digitado é {min(lista)}')
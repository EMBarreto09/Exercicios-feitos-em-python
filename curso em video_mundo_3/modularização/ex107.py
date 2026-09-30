#Moeda

import moeda

v = int(input('Digite o valor do produto: '))
print(f'O Dobro de {v} é igual a {moeda.dobro(v)}')
print(f'A metade de {v} é igual a {moeda.metade(v)}')
print(f'O aumento de {v} com 10% de juros é {moeda.aumentar(v)}')
print(f'A diminuição de {v} com 13% de desconto é {moeda.diminuir(v)}')
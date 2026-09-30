#Melhorando o chamado

import moeda

v = int(input('Digite o valor do produto: '))
print(f'O Dobro de {moeda.moeda(v)} é igual a {moeda.dobro(v, True)}')
print(f'A metade de {moeda.moeda(v)} é igual a {moeda.metade(v, True)}')
print(f'O aumento de {moeda.moeda(v)} com 10% de juros é {moeda.aumentar(v, True)}')
print(f'A diminuição de {moeda.moeda(v)} com 13% de desconto é {moeda.diminuir(v, True)}')
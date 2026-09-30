#Formatação monetária

import moeda

v = int(input('Digite o valor do produto: '))
print(f'O Dobro de {moeda.moeda(v)} é igual a {moeda.moeda(moeda.dobro(v))}')
print(f'A metade de {moeda.moeda(v)} é igual a {moeda.moeda(moeda.metade(v))}')
print(f'O aumento de {moeda.moeda(v)} com 10% de juros é {moeda.moeda(moeda.aumentar(v))}')
print(f'A diminuição de {moeda.moeda(v)} com 13% de desconto é {moeda.moeda(moeda.diminuir(v))}')
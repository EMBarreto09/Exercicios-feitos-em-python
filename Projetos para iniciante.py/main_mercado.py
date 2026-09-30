#Caixa eletrônico

continuar = 's'

lista = []
dicionario_item = {}

print('==================')
print('Mercado da Grau')
print('==================')

while continuar == 's':

    item = str(input('Qual o nome do produto que deseja comprar: '))
    valor = float(input('Qual o valor do produto: '))
    unidade = int(input('Quantas unidades irá levar esse produto:  '))

    dicionario_item[item] = unidade

    print(f'Compra do produto: {item}')
    print(f'Valor: {valor:.2f} à unidade')

    for c in range(1, unidade + 1):
        unidade_valor = valor * c
        valor_total = unidade * valor
        lista.append(valor_total)
        print(f'{c} unidades de {item}: R${unidade_valor:.2f}')

    escolha = str(input('<<<Deseja comprar mais algum item? s ou n >>> ')).lower()

    if escolha == 's':
        continue
    else:
        print(f'Foram comprados estes produtos: {dicionario_item}')
        print(f'Valor total da compra: R${sum(lista):.2f}')
        break

print('Formas de pagamento')
print("""[1] - Dinheiro
[2] - Cartão à vista
[3] - Cartão parcelado em 2 vezes
[4] - cartão parcelado até 3 ou mais vezes""")

escolha_pagamento = str(input('Escolha a forma de pagamento: '))

if escolha_pagamento == '1':
    print(f'O total da compra saiu por: R${sum(lista)}')
elif escolha_pagamento == '2':
    print(f'O total da compra saiu por: R${sum(lista)}')
elif escolha_pagamento == '3':
    valor_cartao = sum(lista) + (sum(lista) * 10/100)
    print(f'O total da compra saiu por: R${valor_cartao}')
elif escolha_pagamento == '4':
    valor_cartao2 = sum(lista) + (sum(lista) * 25/100)
    print(f'O total da compra saiu por: R${valor_cartao2}')

print('Pagamento aprovado')
print('Obrigado pela preferência')
print('Tenha um ótimo dia :)')
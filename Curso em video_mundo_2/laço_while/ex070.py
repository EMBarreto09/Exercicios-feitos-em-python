#Mercado

print('='*30)
print('MERCADÃO DA GRAU')
print('='*30)

cont = 1
menor_preço = 0
menor_nome = ''

executando = True

lista_total = []
contagem_1000 = 0

while executando:
    nome = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o valor do produto: R$ '))

    escolha = str(input('Deseja continuar [S/N]: ')).strip().lower()[0]

    lista_total.append(preço)

    if preço > 1000:
        contagem_1000 += 1

    if cont == 1:
        menor_preço = preço
        menor_nome = nome
        if preço < menor_preço:
            menor_preço = preço
            menor_nome = nome

    cont += 1

    if escolha != 's':
        executando = False
    
print(f'O valor total da compra saiu por: R${sum(lista_total)}')
print(f'Foram {contagem_1000} produtos a mais de R$1000')
print(f'O produto mais barato foi {menor_nome} que saiu por R${min(lista_total)}')


#mercado com tuplas, listas e dicionários

carrinho = []
valor = 0

produtos = {'Arroz': (10.00, 20),
'Feijão': (8.00, 15),
'Macarrão': (5.00, 30),
'leite': (6.00,25)}

minhas_compras = {}

while True:
    print('-'*20)
    print('LOJA')
    print('''1 - Ver produtos
2 - Comprar
3 - Ver total da compra
4 - Sair''')    
    print('-'*20)

    loja = str(input('Escolha uma opção: '))

    if loja not in '1234':
        loja = str(input('ERRO, digite uma opção válida: '))
    if loja == '1':
        print()
        for k, v in produtos.items():
            print(f'{k}: {v}')
    if loja == '2':
        print('='*10)
        print('COMPRAS')
        print('='*10)
        while True:
            minhas_compras.clear()
            minhas_compras['item'] = str(input('Qual item deseja comprar: ')).capitalize()
            minhas_compras['quantidade'] = int(input('Quantos deste item deseja comprar: '))
            
            carrinho.append(minhas_compras.copy())

            escolha = str(input('Deseja comprar mais alguma coisa [s/n]: ')).strip().lower()[0]

            if escolha not in 'sn':
                escolha = str(input('ERRO, digite um opção válida: ')).strip().lower()[0]
            if escolha == 'n':
                break
    if loja == '3':
        print('-'*20)
        print('NOTA FISCAL')
        print('-'*20)

        for compra in carrinho:
            item = compra['item']
            quantidade = compra['quantidade']
            preco = produtos[item][0]
            valor_item = quantidade * preco
            valor += valor_item
            print(f'{quantidade}X de {item} = {valor_item}')
            print(f'Total da compra >>> R${valor}')

    if loja == '4':
        print('Fim programa')
        break

print(carrinho)
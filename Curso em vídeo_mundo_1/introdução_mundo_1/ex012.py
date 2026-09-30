#Desconto no produto

produto = float(input('Digite o valor do produto: '))
 
desc = produto - (produto * 5/100)

print(f'O valor do produto que antes era {produto}\nagora com 5% de desconto irá sair por {desc:.2f}')

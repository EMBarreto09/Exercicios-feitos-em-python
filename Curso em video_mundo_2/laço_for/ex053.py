#Palíndromo

palavra = str(input("Digite uma palavra: ")).strip()

comparacao = palavra

if comparacao == palavra[::-1]:
    print('É um PALÍNDROMO')
else:
    print('Não é um PALÍNDROMO')
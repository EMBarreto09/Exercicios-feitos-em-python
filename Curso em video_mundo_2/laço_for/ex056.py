#Analisador completo
mulheres = 0
velho = 0
nome_velho = ''
lista_nome = []
lista_idade = []
lista_sexo = []

for p in range(1, 5):
    print(f'=========== {p}º PESSOA ===========')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('M/F: '))

    lista_nome.append(nome)
    lista_idade.append(idade)
    lista_sexo.append(sexo)

    if p == 1 and sexo in 'Mm':
        velho = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > velho:
        velho = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres +=1
    
media = sum(lista_idade) / len(lista_idade)

print(f'A média de idade do grupo é de {media} anos')
print(f'A pessoa mais velha tem {velho} anos e se chama {nome_velho}')
print(f'Existem {mulheres} mulheres com menos de 20 anos')

    
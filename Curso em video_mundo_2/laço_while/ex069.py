#Cadastro

continuar = 's'

contagem_mulher = 0
contagem_idade = 0
contagem_homem = 0


while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()[0]

    continuar = str(input('Deseja continuar: [S/N]: ')).strip().lower()[0]

    if idade >= 18:
        contagem_idade += 1

    if sexo in 'mM':
        contagem_homem += 1

    if sexo == 'f' and idade < 20:
        contagem_mulher += 1

    if continuar != 's':
        break
    

print(f'Foram registrados {contagem_idade} pessoas com mais de 18 anos')
print(f'Foram registrados {contagem_homem} homens')
print(f'Foram registrados {contagem_mulher} mulheres com menos de 20 anos')
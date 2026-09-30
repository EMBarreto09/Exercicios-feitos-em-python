#Classificando atletas
from datetime import date

ano = int(input('Ano de nascimento: '))
ano_atual = date.today().year
diferenca_idade = ano_atual - ano

if diferenca_idade <= 9:
    print(f'Você tem {diferenca_idade} anos de idade')
    print('Categoria: [\033[32mMIRIM\033[m]')
elif diferenca_idade <= 14:
    print(f'Você tem {diferenca_idade} anos de idade')
    print('Categoria: [\033[33miNFANTIL\033[m]')
elif diferenca_idade <= 19:
    print(f'Você tem {diferenca_idade} anos de idade')
    print('Categoria: [\033[35mJÚNIOR\033[m]')
elif diferenca_idade <= 25:
    print(f'Você tem {diferenca_idade} anos de idade')
    print('Categoria: [\033[36mSÊNIOR\033[m]')
else:
    print(f'Você tem {diferenca_idade} anos de idade')
    print('Categoria: [\033[31mMASTER\033[m]')
#Alistamento militar
from datetime import date
 
ano = int(input('Ano do seu nascimento: '))
ano_atual = date.today().year

idade = ano_atual - ano
idade_diferenca = 18 - idade
para_18 = idade_diferenca + ano_atual
passou_idade = idade - 18
passou_18 = ano_atual - passou_idade

if idade < 18:
    print(f'Quem nasceu em {ano} tem {idade} anos em {ano_atual}')
    print(f'Ainda faltam {idade_diferenca} anos para o seu alistamento')
    print(f'O seu alistamento será em {para_18}')
elif idade > 18:
    print(f'Quem nasceu em {ano} tem {idade} anos em {ano_atual}')
    print(f'Você já deveria ter se alistado a {passou_idade} anos')
    print(f'Seu alistamento foi em {passou_18}')
else:
    print(f'Quem nasceu em {ano} tem {idade} anos em {ano_atual}')
    print('Você tem que se alistar imediatamente')
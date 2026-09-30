#Maioridade
from datetime import date

maior = 0
menor = 0
atual = date.today().year

for c in range(1, 3):
    ano = int(input(f'Qual o ano de nascimento da {c}º pessoa: '))
    comparacao = atual - ano
    if comparacao >= 21:
        maior +=1
    else:
        menor +=1
        
print(f'{maior} pessoas são de maior')
print(f'{menor} pessoas são de menor')

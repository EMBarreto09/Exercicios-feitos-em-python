#Cadastro em dicionários

cadas = {}

cadas['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimneto: '))
idade = 2026 - nasc
cadas['idade'] = idade
cadas['carteira'] = int(input('Carteira de trabalho (0 se não tem): '))
if cadas['carteira'] != 0:
    cadas['contratação'] = int(input('Ano de contratação: '))
    cadas['salário'] = float(input('Salário: '))
    apos = 65 - idade + 2026
    cadas['aposentadoria'] = apos

for k, v in cadas.items():
    print(f'A chave {k} tem o valor {v}')
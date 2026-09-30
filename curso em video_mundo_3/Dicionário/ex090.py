#Notas no Dicionário

aluno = {}

aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Media'] = float(input('Média do aluno: '))
aluno['Situação'] = 'aprovado' if aluno['Media'] > 7 else 'reprovado'

print(aluno)
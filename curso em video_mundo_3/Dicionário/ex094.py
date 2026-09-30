#Cadastro de pessoas

cad = {}
lista = []
media = soma = 0

while True:
    cad['nome'] = str(input('Nome: '))
    cad['sexo'] = str(input('Sexo [m/f]: ')).strip().lower()[0]
    while cad['sexo'] not in 'mf':
        cad['sexo'] = str(input('ERRO!!, Digite uma opção válida: '))
        if cad['sexo'] in 'mf':
            break
    cad['idade'] = int(input('Idade: '))
    lista.append(cad.copy())
    
    soma += cad['idade']
    media = soma / len(lista)

    escolha = str(input('Deseja continuar [s/n]: ')).strip().lower()[0]
    while escolha not in 'sn':
        escolha = str(input('ERRO!!, digite uma opção válida: '))
    if escolha == 'n':
        break

print(f'Ao todo temos {len(lista)} cadastradas')
print(f'À média de idade é {media}')
print(f'As mulheres registradas foram', end=' ')

for l in lista:
    if l['sexo'] == 'f':
        print(l['nome'], end=' ')
        
print()

print('Pessoas com idade acima da média')
for p in lista:
    if p['idade'] > media:
        print(f'{p['nome']} tem {p['idade']} anos')
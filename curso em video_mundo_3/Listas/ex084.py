#Análise completa com lista

lista_temporaria = []
lista_principal = []
maior = 0
menor = 0

while True:
    lista_temporaria.append(str(input('Nome: ')))
    lista_temporaria.append(float(input('Peso: ')))

    if len(lista_principal) == 0:
        maior = menor = lista_temporaria[1]
    else:
        if lista_temporaria[1] > maior:
            maior = lista_temporaria[1]
        if lista_temporaria[1] < menor:
            menor = lista_temporaria[1]

    lista_principal.append(lista_temporaria[:])
    lista_temporaria.clear()

    escolha = str(input('Deseja continuar [s/n]: ')).strip().lower()[0]

    if escolha not in 'Ss':
        break

print(f'Ao todo foram cadastrados {len(lista_principal)} pessoas')
print(f'A pessoa mais pesada cadastrada tem {maior} KG:', end=' ')
for p in lista_principal:
    if p[1] == maior:
        print(p[0], end=' ')
print()
print(f'A pessoa mais leve cadastrada tem {menor} KG:', end=' ')
for p in lista_principal:
    if p[1] == menor:
        print(p[0], end=' ')
print()

#Calcular ano bissto

ano = int(input('Digite um ano para saber se ele é bissto: '))

if ano %4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissto')
else:
    print(f'O ano {ano} não é bissto')
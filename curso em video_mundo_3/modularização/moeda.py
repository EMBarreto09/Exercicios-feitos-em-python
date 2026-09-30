def aumentar(preço, taxa=10, Formatação=False):
    a = preço + (preço * taxa/100)
    return a if not Formatação else moeda(a)

def diminuir(preço, taxa=13, Formatação=False):
    d = preço - (preço  * taxa/100)
    return d if Formatação is False else moeda(d)

def metade(preço, Formatação=False):
    pre = preço / 2
    return pre if not Formatação else moeda(pre)

def dobro(preço, Formatação=False):
    dob = preço * 2
    return dob if not Formatação else moeda(dob)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def resumo(preço=0, taxaa=0, taxab=0):
    print('-'* 30)
    print('RESUMO DO VALOR'.center(30))
    print('-'* 30)
    print(f'Valor analisado:\t{moeda(preço)}')
    print(f'Dobro de valor: \t{moeda(dobro(preço))}')
    print(f'Metade de valor:\t{moeda(metade(preço))}')
    print(f'Aumentando valor:\t{moeda(aumentar(preço, taxaa))}')
    print(f'Diminuindo valor:\t{moeda(diminuir(preço, taxab))}')
    print('-'* 30)
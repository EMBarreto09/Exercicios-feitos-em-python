#Voto

def lin():
    print('-' * 25)
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos. Não pode votar'
    elif idade < 18 and idade > 15 or idade > 69:
        return f'Com {idade} anos. O voto é opcional'
    else:
        return f'Com {idade} anos. O voto é obrigatório'

nasc = int(input('Ano de nascimento: '))
lin()
print(voto(nasc))
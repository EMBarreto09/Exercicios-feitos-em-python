#Analisador de palavras

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMAR', 'FUTURO')

for p in palavras:
    print(f'\nNa palavra {p} temos', end=' ')
    for l in p.lower():
        if l in 'aeiou':
            print(l, end=' ')
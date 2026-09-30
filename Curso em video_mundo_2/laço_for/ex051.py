#PA

print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

termo = int(input('Termo: '))
razao = int(input('Razao: '))

enezimo = termo + (11 - 1) * razao

for c in range(termo, enezimo, razao):
    print(c, end=' -> ')

print('Fim')
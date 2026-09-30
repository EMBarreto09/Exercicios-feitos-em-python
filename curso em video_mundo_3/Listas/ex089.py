#Boletim

lista = []
lista_1 = []

cont = 0

while True:
    lista.append(str(input("Nome: ")))
    lista.append(float(input("Nota 1: ")))
    lista.append(float(input("Nota 2: ")))

    escolha = str(input("Deseja continuar [s/n]: ")).strip().lower()[0]

    lista_1.append(lista[:])
    lista.clear()

    if escolha != 's':
        break


print()
print("===BOLETIM ESCOLAR===")
print("Nº",end='   ')
print("Nome", end='    ')
print("Média")

for i in lista_1:
    print(f'{cont:<5}{lista_1[cont][0]:<7}', end=' ')
    media = (lista_1[cont][1] + lista_1[cont][2]) / 2
    print(f'{media:.2f}')
    cont += 1
print('-'*20)

while True:
    individual = (int(input('Mostrar notas de qual aluno ou 999 para interromper: ')))
    if individual == 999:
        print('Volte sempre')
        break
    else:
        print('-' * 30)
        print(f'Notas de {lista_1[individual][0]} são:', end=' ')
        print(f'{[lista_1[individual][1]]} {[lista_1[individual][2]]}')
        print('-' * 30)
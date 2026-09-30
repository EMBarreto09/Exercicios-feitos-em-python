#Laço de repetição com tabuada

a = int(input("Digite um número para ver a sua tabuada: "))
i = 0

for i in range(11):
    resul = a * i
    print(f'{a} x {i} = {resul}') 
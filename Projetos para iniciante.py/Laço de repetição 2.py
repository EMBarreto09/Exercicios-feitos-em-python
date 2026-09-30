#Laço de repetição com tabuada

for i in range(1,11):
    print('----------------')
    print(f'TABUADA DO {i}')
    print('----------------')
    for contador in range(11):
        resul = i * contador
        print(f"{i} x {contador} = {resul}")
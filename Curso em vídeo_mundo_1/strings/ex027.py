#Avaliador de nomes

n = str(input('Digite seu nome inteiro: ')).strip()

print('Prazer em te conhecer')
nome = n.split()

print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')
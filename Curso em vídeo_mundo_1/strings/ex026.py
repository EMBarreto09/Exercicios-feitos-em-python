#Verificador de 'A' na frase

frase = str(input('Digite uma frase: ')).lower()

print(f'A letra A aparece {frase.count('a')} vezes na frase')
print(f'A primeira letra A aparece na posição {frase.find('a')+1}')
print(f'A última letra A aparece na posição {frase.rfind('a')+1}')
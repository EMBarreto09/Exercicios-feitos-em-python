#Contador de vogais

palavra = input('Digite uma palavra para sabermos quantas vogais ela tem: ')
contador = 0
vogal = 'aeiouAEIOU'

for l in palavra:
    if l in vogal:
        contador +=1
       
print(contador)
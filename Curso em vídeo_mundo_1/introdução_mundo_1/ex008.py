#Conversor de distâncias

distancia = float(input('Digite a distância em metros: '))

print(f'{distancia / 1000}km')
print(f'{distancia / 100}hm')
print(f'{distancia / 10}dam')
print(f'{distancia * 10:.0f}dm')
print(f'{distancia * 100:.0f}cm')
print(f'{distancia * 1000:.0f}km')
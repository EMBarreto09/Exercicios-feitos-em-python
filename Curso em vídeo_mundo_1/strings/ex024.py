#Verificador de cidade que comece com santo

cidade = input('Digite a cidade que você nasceu: ').strip()

print(cidade[:5].upper() == 'SANTO')


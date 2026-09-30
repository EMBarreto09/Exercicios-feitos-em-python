#Analisando e gerando dicionários

geral = {}

def notas(*num, sit=True):

    geral['total'] = len(num)

    media = 0
    geral['maior'] = num[0]
    geral['menor'] = num[0]

    for i in num:
        if i > geral['maior']:
            geral['maior'] = i
    
    for c in num:
        if c < geral['menor']:
            geral['menor'] = c

    for m in num:
        media += m
        geral['media_total'] = media / len(num)
   
    if sit == True:
        if geral['media_total'] < 5:
            geral['situação'] = 'Ruim'
        elif 6 > geral['media_total'] < 7:
            geral['situação'] = 'Mediana'
        else:
            geral['situação'] = 'Ótimo'
    
    print(geral)

num = notas(5.5, 3.0, 7.3, 2.5, 9.0, 1.9, sit=True)
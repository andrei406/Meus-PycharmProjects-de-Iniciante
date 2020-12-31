lista = str(input('Digite a sua expressão númerica com parentêses: '))
#Uma string também é uma lista
res = list()
for simbolo in lista:
    #As vezes não nomear com c e sim com algo específico é melhor
    #Agora entra em loop e da para parar com um break (o que achei bem estranho
    if simbolo == '(':
        res.append('(')
    elif simbolo == ')':
        if len(res) > 0:
            res.pop()
        else:
            res.append(')')
            break
if len(res) == 0:
    print('Expreção válida')
else:
    print('Não é válida')
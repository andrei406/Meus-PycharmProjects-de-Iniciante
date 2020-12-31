n1 = int(input('Digite a distância em km para ser calculado o preço da passagem:'))
print('0,50 por quilometro se for uma viagem de até 200Km, superior, 0,45')
if n1 <= 200:
    print('O preço é {:.2f}R$'.format(n1 * 0.50))
else:
    print('O preço é {:.2f}R$'.format(n1 * 0.45))

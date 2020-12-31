S = int(input('Á quantos kilometros você está andando?'))
if S < 81:
    print('Está na lei, o limite é 80Km/h')
else:
    print('O limite é 80, a multa é {}'.format((S - 80) * 7))

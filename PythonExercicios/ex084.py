print('Nome e peso')
cadaum = []
tudo = []
pesadao = []
levezao = []
totmaior = totmenor = 0
while True:
    cadaum.append(str(input('Digite o seu nome: ')))
    cadaum.append(float(input('Digite o seu peso: ')))
    if len(tudo) == 0:
        totmenor = totmaior = cadaum[1]
    else:
        if cadaum[1] > totmaior:
            totmaior = cadaum[1]
        elif cadaum[1] < totmenor:
            totmenor = cadaum[1]
    tudo.append(cadaum[:])
    cadaum.clear()
    t = str(input('Quer continuar? '))[0].upper()
    if t == 'N':
        break
print(f'Foram cadastradas {len(tudo)} pessoas')
totmenor = totmaior = tudo[0][1]
print(f'O maior peso foi {totmaior} e seus donos: ')
for p in tudo:
    if p[1] == totmaior:
        print(f'{p[0]}', end=' ')
print(f'\nO peso mais leve foi {totmenor} e o seus donos: ')
for p in tudo:
    if p[1] == totmenor:
        print(f'{p[0]}', end=' ')
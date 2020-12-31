c = t = mc = map = mep = 0
ba = ' '
while True:
    c += 1
    n = str(input(f'Qual é o nome do {c}º produto?' ))
    p = float(input(f'Qual é o preço do {c}º produto? R$'))
    t += p
    if p > map:
        map = p
    if c == 1 or p < mep:
        mep = p
        ba = n
    if p > 1000:
       mc += 1
    f = ' '
    while f not in 'SN':
        f = str(input('Quer continuar? '))[0].upper()
        if f == 'N':
            break
        elif f == 'S':
            break
    if f == 'N':
        break
print(f'O total foi de R${t}, {mc} custaram mais de R$1000 e mais batato foi de {ba} de R${mep}')
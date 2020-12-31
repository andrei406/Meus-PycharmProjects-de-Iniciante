v = int(input('Quer sacar quando? (Valores inteiros) '))
r = cinquenta = vinte = dez = um = 0
#while True:
if v >= 50:
    cinquenta = v // 50
    print(f'Foram sacadas {cinquenta} de cinquenta')
    if v % 50 < 100:
        r = v % 50
        if r >= 20:
            vinte = r // 20
        elif r >= 10:
            dez = r // 10
        elif r > 1:
            um = r // 1
elif v >= 20:
    if v >= 20:
        vinte = v // 20
        r = v % 20
    elif r >= 10:
        dez = r // 10
    elif r > 1:
        um = r // 1
elif v >= 10:
    dez = v // 10
    if r % 10 > 10:
        um = v // 1
elif v >= 1:
    um = v // 1
print(f'De 50 foram {cinquenta}, de 20 foram {vinte}, de 10 foram {dez} e de um foram {um}')
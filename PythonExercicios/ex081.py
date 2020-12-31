lista = []
count = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    count += 1
    while True:
        t = str(input('Quer continuar? '))[0].upper()
        if t == 'S':
            break
        elif t == 'N':
            break
    if t == 'N':
        break
print(f'Foram digitados {len(lista)} números\nLista em forma decrescente: ')
lista2 = sorted(lista)
print(lista2[::-1])

if 5 in lista:
    print('O número cinco apareceu na lista')
else:
    print('o número cinco não apareceu na lista')
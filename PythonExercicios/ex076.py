lista = ('Monitor', 500, 'Teclado', 50, 'Mouse', 30,
         'Caixas de som', 50, 'Fones de ouvido', 30,
         'Fonte de alimentação para PC', 70,
         'Gabinite de PC mais poderoso que um gamer', 3000,
         'Mesa para PC', 100)
print('~' * 20)
print(f'{"THE FUCK LIST OF PC":^20}')
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<70}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print(f'~' * 20)
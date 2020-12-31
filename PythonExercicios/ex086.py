matriz = list()
adicionador = []
for c in range(0, 3):
    for d in range(0, 3):
        adicionador.append(int(input(f'Digite um valor para a posição [{c}, {d}]: ')))
    matriz.append(adicionador[:])
    adicionador.clear()
for c in range(0, 3):
    for d in range(0, 3):
        print(f'[{matriz[c][d]:^5}]', end=' ')
    print('\n', end='')
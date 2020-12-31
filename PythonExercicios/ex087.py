matriz = []
adicionador = []
totpar = tottercol = maiorvalseglin = 0
for c in range(0, 3):
    for d in range(0, 3):
        testagem = int(input(f'Digite um valor para a posição [{c}, {d}]: '))
        if testagem % 2 == 0:
            totpar += testagem
        if c == 2:
            tottercol += testagem
        adicionador.append(testagem)
    matriz.append(adicionador[:])
    adicionador.clear()
for c in range(0, 3):
    for d in range(0, 3):
        print(f'[{matriz[c][d]:^5}]', end=' ')
    print('\n', end='')
print(f'A soma de todos os pares foi {totpar}, o maior valor da segunda linha foi {max(matriz[1])} e soma de'
      f'\ntodos os valorees da terceira linha foi {tottercol}')

from time import sleep
def contador(inicio, fim, passo):
    if inicio > fim:
        if not passo < 0:
            passo *= -1
    if passo == 0:
        passo = 1
    for c in range (inicio, fim + 1, passo):
        if c == inicio:
            sleep(0.5)
        print(c, end=' ')
        sleep(0.5)
    print()


numeros = list()
print('Contagem de 1 a 10 pulando de 1 em 1:')
contador(1, 10, 1)
print('Agora ao inverso w pulando de dois em dois!')
contador(10, -2, -2)
print('Agora é sua vez!')
for c in range(0, 3):
    if c == 0:
        i = 'inicio'
    if c == 1:
        i = 'fim'
    if c == 2:
        i = 'pulo'
    numeros.append(int(input(f'Insira o {i}:')))
contador(numeros[0], numeros[1], numeros[2])
"""O professor falou possiveis erros, então veja as prits
e corrija-as"""
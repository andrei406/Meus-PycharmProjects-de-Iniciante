# FuCK EXERCICIE 100!!!!
from random import randint
numeros = list()


def sorteia():
    for c in range(0, 5):
        numeros.append(randint(0, 11))
def somaPar():
    somapar = 0
    for c in numeros:
        if c % 2 == 0:
            somapar += c
    print(somapar)

sorteia()
print(f'Os valores sorteados foram: {numeros}\n'
          f'e a soma dos pares foi:', end=' ')
somaPar()





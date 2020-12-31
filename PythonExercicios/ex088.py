from random import randint
from time import sleep
d = 1
palpites = []
print('AQUELA AJUDA')
a = int(input('Quantos palpites quer sobre a MEGA SENA? '))
while not d == a + 1:
    for c in range(1, 7):
        palpites.append(randint(1, 61))
    print(f'Jogo nº{d}: {palpites}')
    palpites.clear()
    sleep(1)
    d += 1
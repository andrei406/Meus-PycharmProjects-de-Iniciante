from random import randint
from time import sleep
from operator import itemgetter
contador = 1
recebido = []
jogadores = {}
for c in range(1, 5):
    jogadores[f'jogador {c}'] = randint(1, 6)
racking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in jogadores.items():
    print(f'O {i} tirou {v}')
    sleep(1)
print('==> Ranking <==')
for i, v in enumerate(racking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)


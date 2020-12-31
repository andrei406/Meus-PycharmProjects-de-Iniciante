import random
from time import sleep#faz o computador "dormir"
print('Vamos ver se você adivinha o número que pensei?')
print('=' * 40)
print('Adivinhe o número que pensei de 0 á 10!')
print('=' * 40)
v = random.randint(0, 10) # faz o computador pensar
s = int(input('Digite o número que você acha que é:')) # o jogador tenta adivinhar
print('PENSANDO...')
sleep(3)
if s == v:
    print('Parabéns, ganhou!')
else:
    print('Que pena, perdeu')
    print('Ele era: {}'.format(v))

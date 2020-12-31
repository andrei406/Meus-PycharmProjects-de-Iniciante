import random
import time
print('\033[31mVamos jogar Joquempô!')
print('-=-' * 50)
j = str(input('\033[32mVai de pedra, papel ou tesoura?'))
print('-=-' * 50)
v1 = str('pedra papel tesoura')
v2 = v1.split()
c = random.choice(v2)
time.sleep(1)
print('\033[31m3')
time.sleep(1)
print('\033[38m2')
time.sleep(1)
print('\033[33m1')
print('Escolhi {}!'.format(c))
if j == 'papel' and c == 'pedra':
    print('Você ganho!')
elif c == 'papel' and j == 'pedra':
    print('Eu ganhei!')
elif j == 'pedra' and c == 'tesoura':
    print('Você ganhou!')
elif c == 'pedra' and j == 'tesoura':
    print('Eu ganhei!')
elif c == 'tesoura' and j == 'papel':
    print('Eu ganhei')
elif c == 'papel' and j == 'tesoura':
    print('Você ganhou!')
elif c == j:
    print('Empate!')
else:
    print('\033[4;36mOps, algo deu errado! Tente novamente! Mas sem gracinhas, em?')

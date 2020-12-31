from random import randint
print('VAMOS JOGAR!')
c = 0
jp = ''
while True:
    while True:
        co = randint(0, 9)
        jp = str(input('Par ou ímpar? [P/I]: ')).upper().strip()[0]
        if not jp in 'PI':
            print('NÃO TEM GRAÇA')
        else:
            break
    j = int(input('Agora seu número? '))
    if jp == 'I':
        cp = 'P'
        r = co + j
        if r % 2 == 0:
            print('VOCÊ PERDEU!')
            break
        else:
            print('VOCÊ GANHOU...\nVAMOS NOVAMENTE SORTUDO!')
            cp = jp = ''
            c += 1
            j = co = 0
    else:
        cp = 'I'
        r = c + j
        if r % 2 == 0:
            print('VOCÊ PERDEU!')
            break
        else:
            print('VOCÊ GANHOU...\nVAMOS NOVAMENTE SORTUDO!')
            cp = jp = ''
            c += 1
            j = co = 0

print(f'Você teve {c} vitória(s) consecultiva(s)')
#Nas proximas linhas, sera feito o algoritmo que determinara se o jogador vai ganhar ou perder


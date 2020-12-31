import random
j = 0
c = random.randint(0, 10)
count = 1
g = 0
v = 0
print("\033[36m[-[]]\033[m" * 5)
print('\033[1:32mVamos Jogar!\033[m')
print('\033[36m[-[]]' * 5)
print('\033[31mDe 0 á 10, consegue adivinhar qual eu vou escolher?\033[m')
while g != 1:
    j = int(input('Vamos jogadar: ').lower())
    if c != j:
        print('ERROU!', end='')
        print('Vamos tentar novamente')
        count += 1
        if j < c:
            print('\033[35mMais...\033[m')
        if j > c:
            print('\033[34mMenos...\033[m')
    else:
        print('Você GANHOU!\nMas teve que tentar {} vez(es)'.format(count))
        g += 1

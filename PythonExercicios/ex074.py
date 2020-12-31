from random import randint
c = 0
l = (randint(0, 10), randint(0,10),randint(0, 10), randint(0, 10), randint(0, 10))
print('Números sorteados')
for c in l:
    print(c, end=' ')
print(f'\nesse é o maior: {max(l)}\nesse é o menor: {min(l)}')

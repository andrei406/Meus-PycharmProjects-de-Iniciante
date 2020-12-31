#from maht import factorial
count = 0
n = int(input('Digite um número: '))
print('O fatorial de {} é:'.format(n), end='')
count = n
f = 1
if n == 0:
    f = 0
while count > 0:
    print(' {} '.format(count), end='')
    print('x' if count > 1 else ' = ', end='')
    f *= count
    count -= 1
print(f)

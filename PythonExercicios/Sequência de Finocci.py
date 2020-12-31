c1 = c2 = c3 = 0
t = int(input('Deseja ver até qual indice da sequência de Fibocci? '))
for c in range (1, t + 1):
    if c == 1:
        c1 = 0
        print(c1, end=' ')
    elif c == 2:
        c2 = 1
        print(c2, end=' ')
    elif c == 3:
        c3 = c1 + c2
        print(c3, end=' ')
    else:
        c1 = c2
        c2 = c3
        c3 = c1 + c2
        print(c3, end=' ')
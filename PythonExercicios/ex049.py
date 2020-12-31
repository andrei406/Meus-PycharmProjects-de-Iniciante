n1 = int(input('Digite um número para a exibição de sua tabuada:'))
for c in range(0, 10 + 1):
    print('{}x{}={}'.format(n1, c, n1 * c))
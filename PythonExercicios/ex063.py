print('-' * 29, '\nSequênica de Fibocci\n', '-' * 29)
n1 = int(input('Digite até qual número deseja ver a sequência: '))
count = 3
repet1 = 0
repet2 = 1
repet3 = 0
""" O proximo termo é a soma dos dois anteriores"""
print('{} --> {}'.format(repet1, repet2, end=''))
while not count == n1:
    repet3 = repet1 + repet2
    print(repet3, end=' --> ')
    repet1 = repet2
    repet2 = repet3
    count += 1

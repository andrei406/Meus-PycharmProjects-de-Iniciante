"""
Este programa consiste em identificar qual é o maior e menor peso
entre 5 pessoas
"""
n1 = float(input('Digite seu peso:'))
n2 = float(input('Digite seu peso:'))
n3 = float(input('Digite seu peso:'))
n4 = float(input('Digite seu peso:'))
n5 = float(input('Digite seu peso:'))
for c in range(0, 1):
    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
        print('O maior é {}'.format(n1))
    elif n2 > n3 and n2 > n4 and n2 > n5 and n2 > n1:
        print('O maior é {}'.format(n2))
    elif n3 > n4 and n3 > n5 and n3 > n1 and n3 > n2:
        print('O maior é {}'.format(n3))
    elif n4 > n5 and n4 > n1 and n4 > n2 and n4 > n3:
        print('O maior é {}'.format(n4))
    elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
        print('O maior é {}'.format(n5))
    else:
        print('Há mais de uma pessoa com o mesmo peso de outra')
for c in range (0, 1):
    if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
        print('O menor é {}'.format(n1))
    elif n2 < n3 and n2 < n4 and n2 < n5 and n2 < n1:
        print('O menor é {}'.format(n2))
    elif n3 < n4 and n3 < n5 and n3 < n1 and n3 < n2:
        print('O menor é {}'.format(n3))
    elif n4 < n5 and n4 < n1 and n4 < n2 and n4 < n3:
        print('O maior é {}'.format(n4))
    elif n5 < n1 and n5 < n2 and n5 < n3 and n5 < n4:
        print('O maior é {}'.format(n5))
    else:
        print('Há mais de uma pessoa com o mesmo peso de outra')


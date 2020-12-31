n = str(input('Qual é o seu nome?'))
i = int(input('Qual é a sua idade?'))
s = str(input('Qual é o seu sexo?'))
n1 = str(input('Qual é o seu nome?'))
i1 = int(input('Qual é a sua idade?'))
s1 = str(input('Qual é o seu sexo?'))
n2 = str(input('Qual é o seu nome?'))
i2 = int(input('Qual é a sua idade?'))
s2 = str(input('Qual é o seu sexo?'))
n3 = str(input('Qual é o seu nome?'))
i3 = int(input('Qual é a sua idade?'))
s3 = str(input('Qual é o seu sexo?'))
print('A média de idade do grupo é {}'.format((i + i1 + i2 + i3) / 4))
if s == 'masculino' and i > i1 and i > i2 and i > i3:
    print('{} é o homem mais velho'.format(n))
elif s1 == 'masculino' and i1 > i2 and i1 > i3 and i1 > i:
    print('{} é o homem mais velho'.format(n1))
elif s2 == 'masculino' and i2 > i3 and i2 > i and i2 > i1:
    print('{} é o mais velho'.format(n2))
elif s3 == 'masculino' and i3 > i and i3 > i2 and i3 > i1:
    print('{} é o homem mais velho'.format(n3))
else:
    print('Todos tem a mesma idade')
if s == 'feminino' and i < i1 and i < i2 and i < i3:
    print('{} é a mulher mais nova'.format(n))
elif s1 == 'feminino' and i1 < i2 and i1 < i3 and i1 < i:
    print('{} é a mulher mais nova'.format(n1))
elif s2 == 'feminino' and i2 < i3 and i2 < i and i2 < i1:
    print('{} é a mulher mais nova'.format(n2))
elif s3 == 'feminino' and i3 < i and i3 < i2 and i3 < i1:
    print('{} é a mulher mais nova'.format(n3))
else:
    print('Todas tem a mesma idade')

nome = str(input('Seu nome completo:')).strip()
v = nome.split()
v2 = v[0]
print('o primeiro nome é {}'.format(v2))
print('o último é {}'.format(v[len(v)-1]))

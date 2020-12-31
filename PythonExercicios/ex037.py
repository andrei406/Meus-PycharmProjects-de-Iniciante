print('Vamos fazer conversão em unidades númericas!')
n1 = int(input('Digite o número que quer converter:'))
b = str(input('Quer binário, octal ou hexadecimal?'))
r = b.capitalize()
if r == 'Binário':
    print('Em binário fica {}'.format(bin(n1)[2:]))
elif r == 'Hexadecimal':
    print('Em Hexadecial é {}'.format(hex(n1)[2:]))
elif r == 'Octal':
    print('Em octal é {}'.format(oct(n1)[2:]))
else:
    print('Verifique se digitou corretamente')
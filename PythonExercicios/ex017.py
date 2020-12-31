import math
n1 = float(input('Digite o comprimento do cateto oposto:'))
n2 = float(input('Digite o comprimento do cateto adjacente:'))
hi = math.hypot(n1, n2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
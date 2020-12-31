import math
an = float(input('Digite o âmgulo que quer:'))
seno = math.sin((math.radians(an)))
print('O seno do ângulo {:.2f} mede {:.2f}'.format(an, seno))
co = math.cos(math.radians(an))
print('O cosseno é {:.2f}'.format(co))
ta = math.tan(math.radians(an))
print('a tangente é {:.2f}'.format(ta))

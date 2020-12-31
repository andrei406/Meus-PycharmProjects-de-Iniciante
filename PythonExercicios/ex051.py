""""este programa calcula a razão de uma progressão artmedica e m
mosta os primeiros 10 seguintes números"""
n1 = int(input('Digite o primeiro termo da P.A:'))
n2 = int(input('Agora o segundo:'))
if n1 < n2:
        r = n2 - n1
        print('A razão é {}, a P.A é crescente'.format(r))
        for c in range(0, 10 * r, r):
            print(c)
elif n1 > n2:
        r = n1 - n2
        print('A razão é {}, a P.A é retrociva'.format(r))
        for c in range(10 * r , 1, - r):
            print(r - c)
else:
         print('A P.A é progreciva, a razão é'.format(n1))

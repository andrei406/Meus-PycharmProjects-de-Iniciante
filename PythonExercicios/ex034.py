n1 = float(input('Olá! Digite seu sálario para receber uma alteração em nele:'))
if n1 <= 1250.00:
           print('Seu novo salário é {}'.format(n1 + (n1 * 15// 100)))
else:
    print('Seu novo salário é {}'.format(n1 + (n1 * 10 // 100)))

"""

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número:'))
n4 = int(input('Digite o quarto número:'))
n5 = int(input('Digite o quinto número:'))
n6 = int(input('Digite o sexto número:'))
"""

print('\033[33mSerão comparados 6 números\ne se a dupla formada em ordem sequencial de cima para baixo\nse os dois digitos forem par, a soma será feita.\033[m')
for c in range(1, 6 + 1):
    n1 = int(input('Digite o {} número:'.format('primeiro')))
    n2 = int(input('Digite o {} número:'.format('segundo')))
    if n1 % 2 == 0 and n2 % 2 == 0:
        print('Os dois são pares e a soma deles é {}'.format(n1 + n2))
    else:
        print('\033[31mUm dos dois números é impar \nA soma só é feita se os dois forem pares\033[m')
        import time
        time.sleep(3)
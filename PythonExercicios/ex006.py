n1 = int(input('Digite um número:'))
print('O dobro é:\033[0;34m {}\033[m'.format(n1 * 2), end=' ')
print('O triplo é: \033[0;35m{}\033[m'.format(n1 * 3), end=' ')
print('A raiz quadrada é: \033[0;33m{}\033[m'.format(n1 ** 2))

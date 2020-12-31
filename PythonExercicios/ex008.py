n1 = int(input('Digite a medida (em metros com):'))
print('em cm: \033[4;30;41m{}\033[m'.format(n1 * 10))
print('e em mm: \033[4;30;41m{}\033[m'.format(n1 * 100))
print('\033[0;31mEstmos dando 5% de desconto em qualquer produto!\033[m')
n1 = int(input('\033[0;31mPor favor, insira o produto que quer comprar e mostraremos o novo preço dele:\033[m'))
n2 = n1 * 5 / 100
print('\033[0;31mAgora custa R${}!\033[m'.format(n1 - n2))
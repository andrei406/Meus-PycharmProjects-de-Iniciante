print('\033[30mEste programa faz a soma de númeoros digitados pelo o usuario\nmas só para de pedir números quando a soma de todos eles\nfor maior que 100\033[m')
soma =  0
while True:
    n1 = int(input('\033[31mDigite um número: \033[m'))
    soma += n1
    if soma > 100:
        break
print(f'\033[36mO total foi de {soma}')
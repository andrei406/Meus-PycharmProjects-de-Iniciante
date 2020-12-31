print('~' * 50)
print('{:^30}'.format('Banco CA$H'))
print('~' * 50)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 1:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('~' * 50)
print('Volte sempre!')
print('~' * 50)
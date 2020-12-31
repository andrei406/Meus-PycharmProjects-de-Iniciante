print('Lista numerica de cinco valores')
num = list()
maior = menor = 0
for c in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {c}: ')))
    if maior == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print(f'O maior valor foi: {maior}, nas posições: ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor foi: {menor} e estava nas posições: ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end='')
print(f'\nOs números digitados foram:')
for c in num:
    print(c, end=' ')
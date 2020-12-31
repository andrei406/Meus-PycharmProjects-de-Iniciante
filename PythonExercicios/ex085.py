print('São sete valores')
todos = [[], []]
for c in range(1, 9):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        todos[0].append(valor)
    else:
        todos[1].append(valor)
print(f'A lista dos pares em ordem crescente: {sorted(todos[0])}')
print(f'A lista dos ímpares em ordem crescente: {sorted(todos[1])}')
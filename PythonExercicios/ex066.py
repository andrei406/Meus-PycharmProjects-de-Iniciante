print('O programa vai oarar quando for digitado 999')
soma = count = 0
while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    soma += n
    count += 1
print(f'Foram somados {count} números e o total foi de {soma}')
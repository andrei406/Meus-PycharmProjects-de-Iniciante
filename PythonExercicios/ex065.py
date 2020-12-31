print('Este programa lê varios números inteiros, diz qual foi o menor, o maior e a média!')
r = 'S'
s = 0
c = 0
menor = 0
maior = 0
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
    s += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < maior:
            menor = n
print('A média foi de {}\nO maior foi {} e o menor {}' .format(s / c, maior, menor))

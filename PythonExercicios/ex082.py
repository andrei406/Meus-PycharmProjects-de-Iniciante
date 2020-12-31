#programa leitor de valores e distribuidor de impares e pares
num = []
impar = []
par = []
t = 0
ld = ''
while True:
    num.append(int(input('Digite um valor que quiser: ')))
    t += 1
    while True:
        ld = str(input('Quer continuar? '))[0].upper()
        if ld == 'S':
            break
        if ld == 'N':
            break
    if ld == 'N':
        break
# há uma falha que impede que haja um laço que comece do inicio e vá até o fim da lista
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print('fim')
print(f'Lista original: {num}\nLista com os pares: {par}\nLista com os impares: {impar}')
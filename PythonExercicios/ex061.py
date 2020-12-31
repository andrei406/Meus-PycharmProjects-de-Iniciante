c = 1
n1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))
termo = n1
while c <= 10:
    print('{} ->'.format(termo), end='')
    termo += razao
    c +=1
print('FIM')


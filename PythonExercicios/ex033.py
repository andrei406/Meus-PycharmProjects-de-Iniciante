print('Digite um número de cada vez para saber qual dos três é o maior e o menor')
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
n3 = int(input('Digite mais um valor:'))
menor = n1
if n2 < n1 and n2 < n3:
  menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print('O menor é {}.'.format(menor))


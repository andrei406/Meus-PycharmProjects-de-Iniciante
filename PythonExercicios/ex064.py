n1 = count = totaly = 0
print('Este programa soma os números que digitar, enquanto\nvocê não digitar o número 999.')
n1 = int(input('Digite um número: '))
while n1 != 999:
    count += 1
    totaly += n1
    n1 = int(input('Digite um número: '))
print('Você digitou {} números e a soma de todos eles\nfoi de {}'.format(count, totaly ))
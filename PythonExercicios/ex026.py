nome = str(input('Escreva uma frase:')).upper().strip()
print('A letra A aparece {} na frase'.format(nome.count('A')))
print(' A primeira letra A apareceu na posição {}'.format(nome.find('A')+1))
print('A úlima posição em que a letra A aparece é na {}'.format(nome.rfind('A')+1))



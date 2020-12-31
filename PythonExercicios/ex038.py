print('Insira dois números para serem comparados')
n1 = int(input('\033[36mInsira o primeiro número:'))
n2 = int(input('\033[36mAgora o segundo:'))
if n1 > n2:
    print('\033[35mO primeiro número é o maior!')
elif n1 < n2:
    print('\033[34mO segundo número é o maior!')
else:
    print('\033[39mNão há valor maior, os dois são iguais!')
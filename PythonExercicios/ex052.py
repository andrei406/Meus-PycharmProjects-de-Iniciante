print('\033[33mVamos verificar números primos?\nNa verdade se os que você digitar são realmente\nVamos logo começar!\nVocê pode definir quantas vezes a repetição vai acontecer\033[m')
r = int(input('\033[34mQuntas vezes quer que a operação se repita(digite em números)?\033[m'))
for c in range(1, r + 1):
    n1 = int(input('Digite um número:'))
    if n1 == 2 or n1 == 3 or n1 == 5 or n1 == 7:
        print('Ele é primo!')
    elif n1 == 1 or n1 % 2 == 0 or n1 % 3 == 0 or n1 % 5 == 0 or n1 % 7 == 0:
        print('Não é um número primo')
    else:
        print('É primo!')
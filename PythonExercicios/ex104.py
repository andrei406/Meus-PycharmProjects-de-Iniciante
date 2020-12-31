def leiaint(n):
        if not n.isnumeric():
            while True:
                print('\033[31mERRO: DIGITE UM VALOR INTEIRO')
                n = input('\033[34mDigite um número inteiro: ')
                if n.isnumeric():
                    break
            if n.isnumeric():
                print(f'\033[30mVocê digitou o valor {n}')


n = leiaint(input('Digite um número inteiro: '))


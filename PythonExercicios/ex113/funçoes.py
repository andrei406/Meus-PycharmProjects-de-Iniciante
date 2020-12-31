def leiaint(valor):
    while True:
        try:
            n = int(input(valor))
        except (ValueError, TypeError):
            print('\33[31mVocê não informou corretamente o valore pedido\33[m')
            continue
        except KeyboardInterrupt:
            print(' \33[32mO usuário preferiu não informar o número\33[m')
            return 0
        else:
            return n


def leiafloat(valor):
    while True:
        try:
            n = float(input(valor))
        except (ValueError, TypeError):
            print('\33[31mVocê não informou corretamente o valore pedido\33[m')
            continue
        except KeyboardInterrupt:
            print(' \33[32mO usuário preferiu não informar o número\33[m')
            return 0
        else:
            return n

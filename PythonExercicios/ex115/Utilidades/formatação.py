def formatarmenu(msg):
    """
    Serve para formatar uma mensagem
    :param msg: mensagem a ser inserida
    :return: mensagem formatada
    """
    print('\033[31m~' * len(msg))
    print(msg)
    print('~' * len(msg))
    print('\033[m')


def formatartexto(msg):
    print('~' * 30)
    print(msg)
    print('~' * 30)


def feito():
    print('\33[30mFEITO!\33[m')
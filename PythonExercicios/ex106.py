def printo(msg):
    """
    Serve para formatar uma mensagem
    :param msg: mensagem a ser inserida
    :return: mensagem formatada
    """
    print('\033[30:41m~' * len(msg))
    print(msg)
    print('~' * len(msg))
    print('\033[m')


def ajuda(comando):
    print('\033[30:45m')
    help(comando)

while True:
    printo('Ajuda Py')
    teste = str(input('Deseja ver a documetação de qual código? (digite "fim" para parar) ')).lower()
    if teste == 'fim':
        break
    else:
        ajuda(teste)
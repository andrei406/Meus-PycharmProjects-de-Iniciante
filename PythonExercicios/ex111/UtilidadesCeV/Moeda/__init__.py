def aumentar(num=0, adic=0):
    """
    --> Serve para somar um número com outro
    :param num: Número a ser usado na função
    :param adic: Número para ser almentado em porcentagens
    :return: a porcentagens do de num por adic
    """
    res = adic / 100 * num + num
    return res


def diminuir(num=0, sub=0):
    """
    --> Serve para subtrair um número com o outro
    :param num: Número a ser usado na função
    :param sub: número que vai subtrair com num
    :return: a subtração de num com sub
    """
    res = num - sub / 100 * num
    return res


def metade(num=0):
    """
    --> Serve para dividir por doi um número
    :param num: Número a ser usado para ser divido por dois
    :return: num / 2
    """
    res = num / 2
    return res


def dobra(num=0):
    """
    Está funçãos serve para
    dobrar um valor
    :param num: número a ser inserido
    :return: o dobro de num
    """
    res = num * 2
    return res


def moeda(num=0, moeda='R$', formatar=False):
    """
    --> Serve para formatar um valor em real
    :param num: número
    :return: ex: R$3
    """
    if formatar == False:
        moeda = ''
    teste = str(num)
    teste.replace('.', ',')
    return f'{moeda}{num:.2f}'.replace('.', ',')


def resumo(num):
    '''
    Está função serve para aplicar dotas as
    funções anteriores de uma vez só
    :param num: o número que vai ser utilizado em todo o resumo
    :return: uma tabela com os valores
    '''
    print('-' * 50)
    print('RESUMO DO VALOR')
    print('-' * 50)
    print(f'''
    Preço analizado: {moeda(num):<25}
    Dobro do preço: {moeda(dobra(num)):<20}
    Metade do preço: {moeda(metade(num)):<20}
    80% de aumento: {moeda(aumentar(num, 80)):<20}
    32% de recução: {moeda(diminuir(num, 35)):<20}
    ''')
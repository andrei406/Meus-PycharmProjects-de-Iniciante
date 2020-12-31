def fatorial(num, show=0):
    """

    :param num: É o número a ser calculado o fatorial
    :param show: Exibir ou não o fatorial (opcional)
    :return: retornar o valor da fatorização
    """
    resu = num
    for c in range(num - 1, 0, -1):
        resu = resu * c
    if show == True:
        for c in range(num, 0, -1):
            if c > 1:
                print(c, end=' x ')

            else:
                print(c, end=' = ')
    print(resu)


fatorial(5, show=False)
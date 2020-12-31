def notas(* num, situ=0):
    """
    Está função recebe indefinidas notas de alunos e retorna
    um dicionário com informações
    :param num: pode ser colocadas várias notas de vários alunos
    :param situ: True para exibir a situação do aluno
    :return: Um dicionário com as informações
    """
    info = dict()
    r = 0
    print(num)
    info['Quantidade de notas'] = len(num)
    info['Maior nota'] = max(num)
    info['Menor nota'] = min(num)
    for c in num:
        r += c
    info['Média da turma'] = r / len(num)
    if situ is True:
        if info['Média da turma'] < 7.0:
            info['Situação'] = 'RECUPERAÇÃO'
        else:
            info['Situação'] = 'APROVAÇÃO'
    return print(info)

#Programa Principal
notas(2.2, 5.0, 5, situ=False)
help(notas)
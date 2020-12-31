#Identificador de números
"""Neste desafio tem que criar uma lista com 5 valores e mostrar em ordem sem o sort()"""
num = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    """Aqui temos várias possibilidades: ele pode estar no começo, no meio ou no fim"""
    if c == 0:
        #Aqui é verificado se ele é o primeiro ou o ultimo
        num.append(n)
    elif c > num[-1]:
        num.append(n)
        #Mas se ele fica no meio, tem que fazer a seguinte verificação
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                break
            pos += 1
    """Nesta sistaxe, o objetivo é wncontrar o melhor lugar para se colocar o número na lista """
print(f'Os números em ordem: {num}')
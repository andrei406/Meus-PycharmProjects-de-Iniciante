"""Vai se usar mais funções quando os seus
códigos ficarem muito grandes e repetitivos
def soma(a, b):
    s = a + b
    print(s)


#Programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
#Se pode especificar
soma(a= 3, b= 6)
#Até mesmo mudar a ordem
soma(b= 4, a= 9)"""

"""def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


soma(9, 1)"""

"""def contador(* num):
    print(num)
    #se é criado uma tupla


contador(1, 5, 7)
contador(9, 5, 1, 6, 10)
contador(5, 1, 9, 0)"""

"""def contador(* num):
    for valor in num:
        print(valor, end=' ')
    print()

contador(1, 5, 7)
contador(9, 5, 1, 6, 10)
contador(5, 1, 9, 0)"""

#Também é possivel usar quantidades idefinidas como pode
#ver a seguir
"""def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')
    

contador(1, 5, 7)
contador(9, 5, 1, 6, 10)
contador(5, 1, 9, 0)"""

#Também é possivel usar listas e não só tuplas
# e sem utilizar desempacotamento
"""def dobra (lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [2, 7, 12, 6, 0]
dobra(valores)
print(valores)"""


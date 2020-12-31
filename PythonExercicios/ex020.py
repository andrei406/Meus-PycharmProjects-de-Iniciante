import random
n1 = str(input('Digite o nome do primeiro aluno:'))
n2 = str(input('Digite o nome do segundo aluno:'))
n3 = str(input('Digite o nome do terceiro aluno:'))
lista = [n1, n2, n3]
random.shuffle(lista)
print('a sequência da apresentação é:')
print(lista)

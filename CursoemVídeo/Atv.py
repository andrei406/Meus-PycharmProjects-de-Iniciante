def lin(ms/home/andrei/PycharmProjects/PythonExerciciosg):
    print('-' * 30)
    print(msg)


nomes = dict()
for c in range(1, 11):
    nomes[f'pessoa nº{c}'] = str(input(f'Digite o nome da {c}ª pessoa: '))
lin('Os nomes do cadastrados são:')
for n in nomes.values():
    print(n)
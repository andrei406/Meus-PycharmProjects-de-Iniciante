"""Construa um algoritmo que receba os dados de 4 alunos. Para cada aluno, o programa recebe os dados
na seguinte ordem: nome, faltas e média.
Após o algoritmo receber os dados, o seu programa deverá escrever a listagem dos alunos com base
no modelo abaixo:
Formato da Saída esperada:
Nome – No de Faltas – Média
João Almeida – 12 – 7.1
Simbião Chronos – 0 – 8.9
Alice Lovelace – 0 – 9.1
Matoso Matos – 9 – 6.1"""
dados = list()
aluno = dict()
for c in range(1, 2):
    aluno['nome'] = str(input('Digite o nome do aluno: '))
    aluno['faltas'] = int(input(f'Qual é o número de faltas de {aluno["nome"]}? '))
    aluno['media'] = int(input(f'Qual é a média de {aluno["nome"]}? '))
    dados.append(aluno.copy())
    aluno.clear()
print('-' * 50)
print('Nome    | Nº de Faltas| Média')
for i, v in enumerate(dados):
    print(f'{dados[i]["nome"]:^7} | {dados[i]["faltas"]:^7} | {dados[i]["media"]:^7} ')
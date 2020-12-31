from time import sleep


def formatar():
    print('\33[30mm~\33[m' * 50)


alunos = []
formatar()
repeticoes = int(input('Deseja cadastrar quantas pessoas? '))
formatar()
for c in range(0, repeticoes):
    while True:
        try:
            nomeAluno = str(input('Insira o nome do aluno: '))
            numeroFaltas = int(input('Por favor, número de faltas: '))
            media = float(input('Agora a média: '))
        except(ValueError, TypeError):
            formatar()
            print('infelismente, houve um erro, tente novamente!')
            sleep(3)
        else:
            formatar()
            aluno = [nomeAluno, numeroFaltas, media]
            alunos.append(aluno[:])
            aluno.clear()
            break
formatar()
print('Nomes     | Faltas     | Médias')
for c in alunos:
    print(f'{c[0]:^5}     {c[1]:^5}     {c[2]:^10}')
formatar()





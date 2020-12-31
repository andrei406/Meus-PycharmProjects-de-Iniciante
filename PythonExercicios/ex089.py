tudo = []
aluno = []
p = 0
while True:
    aluno.append(str(input('Qual é o nome do aluno que deseja cadastrar? ')))
    for c in range(1, 3):
        aluno.append(int(input(f'Qual é a sua {c}ª nota?' )))
    media = (aluno[1] + aluno[2]) / 2
    aluno.append(media)
    tudo.append(aluno[:])
    aluno.clear()
    t = str(input('Deseja casastrar mais? '))[0].upper()
    if t == 'N':
        break
print('=~' * 20)
print(f'Nº| Nome | Média')
for i, n in enumerate(tudo):
    print(f'{i} | {tudo[i][0]} | {tudo[i][3]}')
print('=~' * 20)
while True:
    p = int(input('Digite o número do aluno que desejar ver o boletin'
                  ' "999" para parar o programa:'))
    if p == 999:
        break
    print(f'As notas de {tudo[p][0]} foram: {tudo[p][1:3]}')
print('=~' * 20)

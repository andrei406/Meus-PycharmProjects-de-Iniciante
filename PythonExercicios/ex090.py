boletin = {'nome': '', 'média' : 0, 'estado' : ''}
boletin['nome'] = str(input('Nome do aluno: '))
boletin['média'] = float(input('Média do aluno: '))
if boletin['média'] >= 7.0:
    boletin['estado'] = 'APROVADO'
elif boletin['média'] >= 5:
    boletin['estado'] = 'RECUPERAÇÃO'
else:
    boletin['estado'] = 'REPROVADO'
print('[[]]' * 6)
for k, v in boletin.items():
    print(f'{k} é igual a {v}')
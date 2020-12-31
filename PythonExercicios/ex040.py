print('Insira duas notas de um aluno para se dar a média')
n = str(input('Mas primeiro, insira a nome do aluno:'))
n1 = float(input('Coloque a primeira nota:'))
n2 = float(input('Agora a segunda:'))
m = ((n1 + n2) / 2)
if m < 5.0 and m >= 0.0:
    print('{} foi reprovado(a)'.format(n))
elif m > 5.0 and m <= 6.9:
    print('{} vai ter que fazer recuperação'.format(n))
elif m == 7.0 or m > 7.0 and m <= 10.0:
    print('{} foi aprovada!'.format(n))
else:
    print('Dados inválidos!')
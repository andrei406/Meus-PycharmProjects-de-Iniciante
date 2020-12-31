somaidade = 0
mediaidade = 0
totmulher = 0
maioridadehomem = 0
nomevelho = ''
for p in range(1, 5):
    print('-' * 5, '{}ª pessoa'.format(p), '-' * 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]:')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher += 1
mediaidade = somaidade / 4
print('A média do grupo é {}'.format(mediaidade))
print('O homem mais velho é {}'.format(nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher))
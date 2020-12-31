from datetime import date
#também coloque o tempo que falta e o que passou além de procurar falhas
print('É momento de dar as suas informações cidadão para o exercito, para o alistamento.')
sexo = str(input('Qual é o seu sexo? M para masculino e F para feminino:'))
if sexo == 'F':
    print('Vocẽ não precisa fazer o alistamento obrigatorio')
elif sexo == 'M':
    print('Você PRECISA')
    a = int(input('Digite o seu ano de nascimento:'))
    d = date.today().year
    i = (d - a)
    if i < 18:
        saldo = 18 - i
        print('Falta {} anos'.format(saldo))
        ano = saldo + a
        print('Seu alistamento vai ser em {}'.format(ano))
    elif i == 18:
        print('Está na hora meu caro!')
    elif i > 18:
        saldo = i - 18
        print('Não é mais hora! Foi há {} ano(s) atrás. '.format(saldo))
        ano = saldo - a
        print('Seu alistamento foi em')

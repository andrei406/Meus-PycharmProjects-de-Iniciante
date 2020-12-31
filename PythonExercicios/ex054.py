from datetime import date
print('Este programa lê o nome de sete pessoas e mostra quem é de maior e que é de menor\n'
      'Será solicitado o nome e a data de nascimento')
at = date.today().year
print(at)
for c in range(0, 7):
    p1 = str(input('Digite seu nome:'))
    p2 = int(input('Seu ano de nascimento:'))
    r = p2 - at
    if r < 20:
        print('É menor de idade')
    else:
        print('É maior de idade')

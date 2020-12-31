i = mi = mmi = h = m = m2 = 0
s = ''
c = 1
while True:
    while True:
        s = str(input(f'Qual é o sexo da {c}ª pessoa? '))[0].upper()
        if s == 'M':
            h += 1
            break
        elif s == 'F':
            m += 1
            break
        else:
            print('Esse sexo não existe')
    pi = int(input(f'Qual é a idade da {c}ªpessoaa? '))
    if  s == 'F':
        if pi < 20:
            m2 += 1
    if pi < 18:
        mi += 1
    if pi >= 18:
        mmi += 1
    while True:
        lg = str(input('Quer registrar mais pessoas?' ))[0].upper()
        if lg == 'N':
            c += 1
            break
        elif lg == 'S':
            c += 1
            break
    if lg == 'N':
        break
print(f'Há {mi} menore(s) de idade, {mmi} de maioridade. Foram cadastrados {h} homem(ns) e há {m2} mulhere(s) com nenos de 20 ano(s)')
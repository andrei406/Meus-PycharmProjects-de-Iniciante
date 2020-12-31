c = 0
nomes = ''.split()
while True:
    nomes += str(input('\033[35mDigite o seu nome convidado: \033[m')).split()
    p = str(input('\033[30mHá mais gente? \033[m'))[0].upper()
    if p == 'N':
        break
print(f'\033[36mOs convidadoes foram:{nomes}\033[m')
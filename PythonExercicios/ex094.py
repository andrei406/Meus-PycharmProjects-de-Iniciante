galera = []
pessoas = dict()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F] '))[0].upper()
        if pessoas['sexo'] in 'MF':
            break
        print('Sexo inestente, tente outra vez')
    pessoas['idade'] = int(input('Idade: '))
    galera.append(pessoas.copy())
    soma += pessoas['idade']
    while True:
        chave = str(input('Quer continuar? [S/N] '))[0].upper()
        if chave in 'SN':
            break
        print('Erro')
    if chave == 'N':
        break
media = soma / len(galera)
print('&' * 46)
print(f'Foram cadastradas {len(galera)} pessoas')
print(f'A média foi {media:5.2f}')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=', ')
print()
print('pessoas acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print(' ')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print('ENCERRADO')
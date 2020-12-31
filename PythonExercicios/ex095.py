times = list()
jogador = dict()
partidas = []

while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Qual é o nome do jogador? '))
    tot = int(input(f'Jogou quantas partidas o {jogador["nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'    Forma feitos quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    times.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? '))[0].upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('=' * 40)
for k, v in enumerate(times):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=' * 40)
while True:
    busca = int(input('Mostra dados de qual jogador? (999 para para parar) '))
    if busca == 999:
        break
    if busca >= len(times):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f'~~~ Levantamento do jogador {times[busca]["nome"]}:')
        for i, g in enumerate(times[busca]['gols']):
            print(f'    No jogo {i} fez {g} gols.')
        print('-' * 40)
print('VOLTE SEMPRE!')

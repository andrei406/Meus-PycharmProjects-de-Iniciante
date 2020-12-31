jogador = dict()
partidas = []
jogador['nome'] = str(input('Qual é o nome do jogador? '))
tot = int(input(f'Jogou quantas partidas o {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Forma feitos quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
#sum é para somar
print('=' * 20)
print(jogador)
print('=' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 20)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} paritdas ')
for i, v in enumerate(jogador['gols']):
    print(f'    Na partida {i} fez {v} gols')
print('=' * 20)
print(f'Foi um total de {jogador["total"]} gols')
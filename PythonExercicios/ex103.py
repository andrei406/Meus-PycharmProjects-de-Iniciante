def ficha(nome_do_jogador, gols):
    print(f'O nome do jogador é {nome_do_jogador}\nE fez {gols} gols ')


nome = str(input('Nome do jogador: '))
if nome == '' or not nome.isalpha():
    nome = 'Desconhecido'
gols = str(input('Gols: '))
if not gols.isnumeric():
    gols = 0
ficha(nome, gols)
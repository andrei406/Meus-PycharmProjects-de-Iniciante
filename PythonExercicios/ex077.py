t = 0
palavras = ('comida', 'peperone', 'caderno', 'arroz', 'salame', 'chinelo', 'armario', 'sopa')
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos', end=' ')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

print('Vamos dar inicio ao processo de empréstimo bancário para a compra de uma casa')
v1 = float(input('Qual é o valor da casa? R$'))
v2 = float(input('Qual é a sua renda mensal? R$ '))
v3 = int(input('Em quantos anos quer pagar?'))
# A parcela mensal não pode exceder 30% do sálario
m = v2 * 30 / 100
# o calculo de m se refere  a mensalidade em anos por isso, v3 é multiplicado por 12
p = v1 / (v3 * 12)
#print(p)
# if p <= 30:
print('Você tem condições')
print('Você pagara uma casa de {} durante {} anos'.format(v1, v3), end='')
# end='' - serve para dizer que não vai aparecer nada no fim da linha
print('A prestação vai ser de R${:.2f}'.format(p))
# else:
# print('Você não tem condições!')
#print(' Coparando: tem que pagar {} e o mínimo é {}'.format(m, p))
if p <= m:
    print('O empréstimo pode ser feito')
else:
    print('Empréstino negado')
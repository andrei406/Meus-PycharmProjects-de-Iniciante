"""programa que consiste em calcular o preço de um produto de acordo com
a forma escolhida"""
p = float(input('Seja bem vindo, cliente! '
                '\n Digite o preço do produto que comprou '
                '\n para para prosseguir a compra:'))
f = str(input('Agora escreva a forma de pagamento \n '
              'a vista \n a vista no cartão '
              '\n em até 2 vezes no cartão '
              '\n 3 vezes no cartão ou mais:'))
if f == 'a vista':
    print('São 10% de desconto nesta forma de pagamento \n ficando por {} a sua compra'.format(p - (p * 10 / 100 )))
elif f == 'a vista no cartão':
    print('São 5% de desconto, ficando então por: {}'.format(p - (p * 5 / 100)))
elif f == 'em até 2 vezes no cartão':
    print('Em até duas vezes no cartão vai ficar duas parcelas de: {}'.format(p / 2))
elif f == '3 vezes no cartão ou mais':
    print('O limite minimo é de 3 parcelas e o maximo é de 10!')
    pa = int(input('Digite em quantas parcelas quer pagar:'))
    if pa >= 3 and pa <= 10:
        print('Serão {}, com o preço de {} (cada),'.format(pa, (p - (pa * 20) / 100)))
    else:
        print('Dados inválidos')
else:
    print('Dados inválidos')
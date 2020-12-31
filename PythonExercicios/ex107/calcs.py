from ex107 import moeda

num = float(input('Digite o valor em reais: R$'))
print(f'Aumentando 10% de resulta em R${moeda.aumentar(num, 10)}')#Tem que preparar a função
print(f'A metade de {num} é {moeda.metade(num)}')
print(f'O dobro de {num} é {moeda.dobra(num)}')
print(f'Diminuindo 13% resulta em {moeda.diminuir(num, 13)}')

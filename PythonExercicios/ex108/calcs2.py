from ex108 import moeda

#num = int(input('Digite o valor em reais: R$'))
num = 10
print(f'Aumentando 10% de {moeda.moeda(num)} resulta em {moeda.moeda(moeda.aumentar(num, 10))}')#Tem que preparar a função
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobra(num))}')
print(f'Diminuindo 13% de {moeda.moeda(num)} resulta em {moeda.moeda(moeda.diminuir(num, 13))}')
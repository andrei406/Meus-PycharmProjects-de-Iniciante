from moeda import moeda, aumentar, metade, dobra, diminuir

#num = int(input('Digite o valor em reais: R$'))
num = 10
print(f'Aumentando 10% de {moeda(num)} resulta em {moeda(aumentar(num), formatar=False)}')#Tem que preparar a função
print(f'A metade de {moeda(num)} é {moeda(metade(num), formatar=False)}')
print(f'O dobro de {moeda(num)} é {moeda(dobra(num), formatar=False)}')
print(f'Diminuindo 13% de {moeda(num)} resulta em {moeda(diminuir(num, 13), formatar=False)}')
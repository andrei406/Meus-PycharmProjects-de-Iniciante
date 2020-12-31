#Se colocar uma estrutura dentro de uma outra estrutura, se mudada-la, onde ela for colocada, também
"""test = list()
test.append('Gustavo')
test.append(40)
galera = list()
galera.append(test)
test[0] = 'Maria'
test[1] = 22
galera.append(teste)
print(galera)"""

#Para evitar isso, basta copiar a lista em vez de colocar dentro de outra
"""test = list()
test.append('Gustavo')
test.append(40)
galera = list()
galera.append(test[:])
test[0] = 'Maria'
test[1] = 22
galera.append(test[:])
print(galera)"""

#Outra forma de adicionar é assim
galera = [['João', 19], ['Ana', 33], ['Joaquin', 13], ['Maria', 45]]
#print(galera)
#print(galera[0])
#print(galera[0][0])
"""for p in galera:
    print(p)
for p in galera:
    print(p[0])
for p in galera:
    print(f'{p[0} tem {p[1} anos de idade')
    """
#Aqui vai exibir os nomes.txt que der, vai copiar e vai exibir, se colocasse, assim que desse clear, ía ficar tudo vázio
"""galera = list()
dado = list()
totm = totme = 0 #Só da para declarar váriaveis simples assim, se fizer isso com as compostar, bem, se alterar uma, altera tudo
for c in range(0,5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
#Para exibir apenas os maiores
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totm += 1
    else:
        print(f'{p[0]} é menor de idade')
        totme += 1
print(f'O total de menor foi {totme} e o de maior {totm}')"""
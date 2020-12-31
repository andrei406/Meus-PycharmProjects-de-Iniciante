par = 0
print('Vamos ler números?')
lista = (int(input('O primeiro valor: ')),
         int(input('Agora o segundo: ')),
         int(input('O penúltimo valor: ')),
         int(input('Digite a último valor: ')))
print(f'Você digitou os valores {lista}')
for c in lista:
    if c % 2 == 0:
        par += 1
print(f'O número quatro repetiu {lista.count(9)} vez(es)')
if 3 in lista:
    print(f'A primeira vez que apareceu 3 foi na posição: {lista.index(3)}')
print(f'Houve {par} números pare(s)')

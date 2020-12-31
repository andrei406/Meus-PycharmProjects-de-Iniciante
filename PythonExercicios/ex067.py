print('Tabuada atualizada [Para parar, basta digitar um número negativo!]')
while True:
    n = int(input('Digite o número do qual deseja visualizar a tabuada:'))
    if n < 0:
        print('Proorama finalizado')
        break
    c = 1
    while c <= 10:
        print(f'{c} x {n} = {c * n}')
        c += 1
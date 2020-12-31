f = 0
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Agora o segundo:'))
print('Digite\n'
      '[1] para somar\n'
      '[2] para multiplicar\n'
      '[3] maior\n'
      '[4] novos números\n'
      '[5] sair do programa\n'
      'Exemplo:\n'
      'Sua resposta: 5')
while f == 0:
    print('=-=' * 15)
    r = int(input('Sua resposta: '))
    print('=-=' * 15)
    if r == 1:
        print('A soma de {} e {} é {}'.format(n1, n2, n1 + n2))
    elif r == 2:
        print('A multiplicação de {} e {} é {}'.format(n1, n2, n1 * n2))
    elif r == 3:
        if n1 > n2:
            print('O mairo número é {}'.format(n1))
        if n2 > n1:
            print('O maior número é {}'.format(n2))
    elif r == 4:
        n1 = float(input('Digite o novo valor: '))
        n2 = float(input('Digite o segundo novo valor: '))
    elif r == 5:
        f = 1
        print('=-=' * 15)
    else:
        print('A opção selecionada NÃO EXISTE')
#7:14
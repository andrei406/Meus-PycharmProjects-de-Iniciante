print('Digite um número entre 0 e 20, em númerico')
n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        p = int(input('Digite um número inteiro e veja a mágica: '))
        if p >= 0 and p <= 20:
            break
    print(f'Você digitou o número {n[p]}')
    t = str(input('Quer continuar? '))[0].upper()
    if t == 'N':
        break

from datetime import date
print('Sejá bem vindo ao meditor de classificações para atletas!')
i = int(input('Agora seu ano de nascimento:'))
at = date.today().year
r = (at - i)
if r <= 9 and r < 14:
    print('Sua categoria é mirim')
elif r <= 14 and r < 19:
    print('Sua categoria é infantil')
elif r == 19 and r < 25:
    print('Sua categoria é junior')
elif r == 25:
    print('Sua categoria é sênior')
elif r >= 20 and r < 100:
    print('Sua categoria é master')
else:
    print('Dados inválidos')
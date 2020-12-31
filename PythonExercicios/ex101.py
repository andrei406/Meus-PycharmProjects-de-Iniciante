def voto(anodenasc):
    from datetime import date
    idade = date.today().year - anodenasc
    if idade == 16 or idade == 17 or idade >= 60:
        return print('O seu voto é OPCIONAL')
    elif idade > 18:
        return print('O seu voto é OBRIGATÓRIO')
    else:
        return print('O seu voto NÃO É PERMITIDO')


resp = int(input('Ano em que nasceu? '))
voto(resp)
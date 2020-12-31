from  datetime import date
n1 = int(input('Vamos saber se o ano que quer saber é bixesto ou não, baste digita-lo aqui, se quiser o ano atual, basta digitar 0:'))
v = n1 % 4
if v == 0:
    v = date.today().year
if v == 0 and v % 100 != 0 or v % 400 == 0:
    print(n1, 'é bixesto')
else:
    print(n1, 'não é bixesto')

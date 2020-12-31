print('Vamos calcuclar o seu IMC!')
p = float(input('Qual é o seu peso:'))
a = float(input('Qual é a sua altura:'))
imc = (p / (a ** 2))
if imc < 18:
    print('\033[30mEstá abaixo do peso')
elif imc >= 18.5 and imc <= 24.9:
    print('Está no peso normal')
elif imc >= 25 and imc <= 29.9:
    print('Está sobre peso')
elif imc >= 30 and imc <= 34.9:
    print('Está na obesidade de grau 1')
elif imc >= 35 and imc <= 39.9:
    print('Está na obesidade de grau 2')
elif imc > 40:
    print('Está na obesidade de grau 3')
else:
    print('Dados inválidos')
print('seu IMC é {:.2f}'.format(imc))

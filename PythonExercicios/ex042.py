print('Vamos descobrir qual triângulo formar!')
"""
Condição de existência de triângulo em python


Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra: um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados. Veja o resumo da regra abaixo:
| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b
"""
print('Vamos descobrir se há como formar um triângulo com medidas que me der.')
a = float(input('primeiro segmento:'))
b = float(input('segindo segmento:'))
c = float(input('terceiro segmento:'))
if a < b + c and b < c + a and c < b + a:
    print('Forma sim um triâmgulo')
    if a == b == c:
        print('É um triângulo  equilatero')
    elif a != b != c != a:
        print('É um triângulo escaleno')
    else:
       print('Forma um triângulo isorceles')
else:
    print('Não forma um triângulo')

from datetime import date
informaoes = {'nome' : '', 'ano de nascimento' : '', 'idade' : 0, 'CTSP' : 0}
datatual = date.today().year
informaoes['nome'] = str(input('Digite seu nome: '))
informaoes['ano de nascimento'] = int(input('Digite seu ano de nascimento: '))
informaoes['idade'] = datatual - informaoes['ano de nascimento']
informaoes['CTSP'] = int(input('Digite sua CTSP (se não temm, digite "0"): '))
if informaoes['CTSP'] > 0:
    informaoes['ano de contratação'] = int(input('Digite o seu ano de contratação '))
    informaoes['salario'] = float(input('Digite o valor de seu sálario: '))
    if informaoes['idade'] <= 60:
        informaoes['falta tantos anos para se aposentar'] = 75 - informaoes['idade']
    elif informaoes['idade'] >= 60:
        informaoes['quando vai se aposentar'] = informaoes['idade'] + 15
print('*' * 50)
for k, v in informaoes.items():
    print(f'{k}: {v}')

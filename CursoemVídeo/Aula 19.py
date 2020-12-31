#Básicão
"""pessoas = {'nomes' : 'Gustavo', 'sexo' : 'M', 'idade' : 22}
print(pessoas)
print(pessoas['nomes'])
#Qundo se quer utilizar aspas de aspas, use duplas se estiverem dentro de unicas e assim vice-versa
print(f'O {pessoas["nomes"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
print()
#print() quebra linha
#Nos dicionairos não utiliza o enumerate, mas sim os itens
for k, v in pessoas.items():
    print(f'{k} = {v}')
del pessoas['sexo']
pessoas['nomes'] = 'Leanro'
pessoas['peso'] = 98.5"""

#diciónarios dentro de listas
"""brasill = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla' : 'RJ'}
estado2 = {'uf' : 'São Paulo', 'sigla' : 'SP'}
brasill.append(estado1)
brasill.append(estado2)
print(brasill[0]['sigla'])
"""
#Caracteristica legal
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    #Como em uma lista para copiar tem que usar [:] em dicionarios é.copy()
    brasil.append(estado.copy())
"""print(brasil)
for e in brasil:
    print(e)"""
for e in brasil:
    """"for k, v in e.items():
        print(f'O campo {k} tem valor {v}')"""

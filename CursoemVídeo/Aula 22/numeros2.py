from Aula.uteis import numeros

#É recomendada importar tudo porque pode haver um bug se houver mais de
#uma biblioteca com a mesma função, se isso acontece, a última vai ser a utilizada
num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')

valores = []
#primero se cria o primerio laço em loop e cria um identificador para saber se o numero
#já está na lista, pois se estiver, deve ser descartado
while True:
    """Coloquei o camando valores.sort() e não funciona, talvez usando valores insert
    se o valor for menor que o menor no lugar dele e outras coisas do tipo, eu nem precise
    articular uma forma no final, só o print mesmo"""
    teste = int(input('Digite um valor: '))
    if teste in valores:
        print('Esse número já está na lista')
    else:
        valores.append(teste)
    while True:
        t = str(input('Quer continuar? ')).upper().split()[0]
        if 'S' in t:
            break
        elif 'N' in t:
            break
    if t == 'N':
        break
#Agora é mostrar a lista em ordem crescente
print('Os valores digitados foram:')
for c in sorted(valores):
    print(c, end=' ')


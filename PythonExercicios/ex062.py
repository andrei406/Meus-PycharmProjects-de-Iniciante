n1 = int(input('Digite o primeiro termo da PA: '))
n2 = int(input('Digite agora a razão da PA: '))
c = 0
s = n1
q = 10
ch = True
t = 10
while ch == True:
    while c != q:
        print(s, end=' --> ')
        s += n2
        c += 1
    q = int(input('\nQuantos mais termos quer ver? Caso não queira mais ver\nDigite 0: '))
    c = 0
    t += q
    if q == 0:
        ch = False
print('Forão mostrados {} termos'.format(t))
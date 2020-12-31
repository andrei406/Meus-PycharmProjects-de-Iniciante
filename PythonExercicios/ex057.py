s = str(input('Digite o seu sexo [M/F]: ')).upper()[0].strip()
while not 'M' and 'F' in s:
    print('Só aceito M ou F para o sexo\nM para masculino e F para feminino!')
    s = str(input('Digite novemente seu sexo [M/F]: ')).upper()
print('Seu sexo foi registrado!')
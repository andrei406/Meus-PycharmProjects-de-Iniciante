arquivo = open('nomes.txt', 'a+')
nome = input('Insira um novo nome: ')
idade = input('Insira a sua idade: ')
arquivo.write(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
              f'\n{nome} {idade:>30}\n')
print('\33[30mPessoa adicionada com sucesso!\33[m')
print('~' * 40)
arquivo.close()

from ex115.Utilidades.formatação import formatartexto
formatartexto(f'A lista com todos é essa:')
arquivo = open('nomes.txt')
print(arquivo.read())
arquivo.close()
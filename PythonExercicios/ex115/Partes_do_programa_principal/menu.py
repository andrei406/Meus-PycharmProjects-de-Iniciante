from ex115.Utilidades.formatação import formatarmenu, formatartexto
while True:
    formatarmenu('MENU PRINCIPAL')
    formatartexto('\33[32m1 - Para ver os nomes.txt já cadastrados\33[m\n'
                  '\33[30m2 - Adicionar mais nomes.txt\n\33[m'
                  '\33[34m3 - Encerrar o programa\33[m')
    while True:
        try:
            resposta = int(input('Insira a sua decisção: '))
        except ValueError:
            print('\33[31mÉ aceito apenas números inteiros\33[m')
        else:
            if resposta == 1:
                from ex115.Partes_do_programa_principal import opção1
            elif resposta == 2:
                from ex115.Partes_do_programa_principal import opção2
            elif resposta == 3:
                print('Programa encerrado. Volte sempre!')
                break
            else:
                print('\33[31mNÃO EXISTE ESSA OPÇÃO!\33[m')
    break

def leiaDinheiro(num):
    valido = False
    while not valido:
        entrada = str(input(num)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print('\033[31mERRO! VALOR NÃO NUMÉRICO\033[m')
        else:
            valido = True
            return float(entrada)
from time import sleep
#from lib.EstruturaTeste import teste
while True:
    print(
    """\33[1;39;40mPORTA DAS ALMAS 
        O JOGO
    
    1. Iniciar
    2. Ajuda
    3. Encerrar    
        """)
    totopc = 3
    try:
        resposta = int(input('\33[39;40mSua escolha: '))
    except KeyboardInterrupt:
        print('\n\33[31mO Jogo interrompido pelo usuário')
    except ValueError:
        print('\33[31;40mO valor informado não é válido\33[m')
    
    else:
        if resposta > totopc:
            print('\33[31;40mO valor informado não é válido\33[m')
        else:
            print()
    if resposta == 1:
        print('\33[39;40mINICIANDO', end='')
        for c in range(0, 3):
            sleep(1)
            print('.', end='')
        print()
        from Episódio1 import execultar
        sleep(5)
    elif resposta == 2:
        print(
"""Está é uma versão do game baseada apenas em um script
que se segue por meio de respostas por meio de um teclado
""")
    elif resposta == 3:
        break


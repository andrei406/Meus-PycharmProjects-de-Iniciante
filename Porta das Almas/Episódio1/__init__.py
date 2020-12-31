from lib.Falas import *
from time import sleep
garota = Falas('Protagonista')
game = Falas('PC')


def estrutura_de_procura(txt, e1='', e02='', e2='', e03='', e3=''):
    decisao = 0
    escolha = 0
    while True:
        if decisao == 2:
            break
        sleep(5)
        game.instrucoes(txt)
        escolha = int(input('Informe sua escolha: '))
        if decisao == 1:
            garota.falaPersorTempReal(e1)
        elif escolha == 2:
            garota.falaPersorTempReal(e02)
            garota.falaPersorTempReal(e2)
            decisao += 1
        elif escolha == 3:
            garota.falaPersorTempReal(e03)
            garota.falaPersorTempReal(e3)
            escolha += 1


def estrurura_de_abrir_porta(txt, e1='', e02='', e2='', e03='', e3=''):
    game.instrucoes(txt)
    sleep(3)
    while True:
        escolha = int(input('Informe sua escolha: '))
        if escolha == 1:
            garota.falaPersorTempReal(e1)
            break
        elif escolha == 2:
            garota.falaPersorTempReal(e02)
        elif escolha == 3:
            garota.falaPersorTempReal(e2)
    sleep(3)


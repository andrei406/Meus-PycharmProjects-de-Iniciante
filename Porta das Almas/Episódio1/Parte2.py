from lib.ObjetosCasa import *
from Episódio1 import *

decisao = 0

garota.falaPersoNarr1P(
"""
O despertar

Eu acordo por volta das 23:00 horas em meu quarto, estava sentindo muito calor
resolvi me levantar, já que o meu sono havia acabado.
Aquele momento para mim era estranho, pois eu ouvia uma voz
me chamando e que dizia que estava me esperando. Olhei pela janela
e vi que era noite de lua cheia, a floresta onde ficava a minha casa estava bastante
iluminada.
"""
)
sleep(10)
estrutura_de_procura("""
    Objetivo:
        • Sair da casa
    Opções:
        1. Explorar o quarto
        2. Ir a cozinha
        3. Ir a sala
""",
    'O meu quarto está organizado, tudo está em perfeita ordem',
    'Na cozinha há uma porta dos fundos',
    'A porta está fechada!',
    'Na sala há uma porta de entrada da casa','A porta está fechada!', )
sleep(3)
print()
garota.falaPersorTempReal('Todas as duas portas da casa estarão trancadas,'
                          '\neu terei que encontrar a chave que levara a saída da mesma')
estrurura_de_abrir_porta(
"""
      Opções:
        1. Procurar na sala:
        2. Procurar na cozinha
        3.Procurar no quarto
""", 'Encontrei a chave!\n'
    'Abro a porta da frente e sigo a voz que continuava a me guiar...',
        'nada...',
        'Não encontro essa chave por aqui')

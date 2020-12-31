from lib.Falas import *
from Episódio1 import *
sleep(3)
e1 = e2 = e3 = False



garota.falaPersoNarr1P(
"""Em mais uma noite eu me encontro em meu quarto buscando onde é que ele está.
Eu já procurei tantas vezes e nunca encontro…
Mas desta vez, eu não vou descansar até encontrá-lo!
""")
while not e1 == e2 == e3 == True:
    sleep(10)
    game.instrucoes("""
    Objetivo:
    • Encontrar algum registro dele
    Opções:
        1. Buscar na internet
        2. Buscar em fotos
        3. Buscar em anotações""")
    sleep(1)
    escolha = int(input('Informe sua decisão: '))
    if escolha == 1:
        garota.falaPersorTempReal(
    """
    Talvez eu tenha deixado algum registro dele por aqui… 
    Olhando aqui em um Chan onde falo sobre sua existência,
    só vejo que essas pessoas me chamam de louca. Alguns até tentam
    me ajudar de alguma forma, como um consolo, mas me dizem que ele não é realmente real…""")
        e1 = True
    elif escolha == 2:
        garota.falaPersorTempReal(
    """
    Eu tirei muitas fotos com ele… Mas ele não aparece em nenhuma!""")
        e2 = True
    elif escolha == 3:
        garota.falaPersorTempReal(
    """
    A última que vez eu vi ele faz muito tempo, as minhas
    anotações são muito tristes desde o seu desaparecimento.
    As que eu ainda vi ele, descrevem como alguém que jamais poderia sumir
    da minha vida, ao menos, era isso que eu achava…""")
        e3 = True


import urllib
import urllib.request
""" Não importa o que pedirem para fazer
com certeza, tem alguma biblioteca que faz o que você precisa"""

try:
    site = urllib.request.urlopen('https://www.oi.com.br')
except:
    print('erro')
else:
    print('tudo ok')

from urllib import request
from urllib.error import URLError


def testa_url():
    try:
        request.urlopen("http://www.pudim.com.br/")
        print('Site está online.')
    except URLError:
        print('O site não está acessível no momento.')


testa_url()

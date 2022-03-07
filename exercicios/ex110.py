# Desafio 110

import locale
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')


def metade(valor):
    return locale.currency(valor/2)


def dobro(valor):
    return locale.currency(valor*2)


def aumenta10(valor):
    return locale.currency(valor*1.1)


def diminui20(valor):
    return locale.currency(valor*0.8)


def resumo(p):
    print(f'A metade de {p} é {metade(p)}')
    print(f'O dobro de {p} é {dobro(p)}')
    print(f'O valor de {p} aumentado 10% é {aumenta10(p)}')
    print(f'O valor de {p} diminuido 20% é {diminui20(p)}')

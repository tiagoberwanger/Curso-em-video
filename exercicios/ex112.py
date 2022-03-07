# Desafio 112

def valida_dinheiro(p):
    while p.isalpha():
        p = input('Valor incorreto! Digite um valor monetário: ')
    return float(p)

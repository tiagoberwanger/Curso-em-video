# Desafio 113

def leia_inteiro_com_tratamento():
    try:
        numero = int(input('Digite um número inteiro: '))
    except Exception as erro:
        print(f'Valor inválido. Erro de: {erro.__class__}.')
    else:
        print(f'Você digitou o número {numero}')


leia_inteiro_com_tratamento()

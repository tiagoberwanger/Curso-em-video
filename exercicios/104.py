# Desafio 104

def leia_inteiro(numero):
  """
    Lê somente números inteiros.
    Qualquer outro input retorna erro.
  """
  if type(numero) is int:
    return f'Você digitou o número {numero}'
  else:
    return f'ERRO! Digite um número válido.'
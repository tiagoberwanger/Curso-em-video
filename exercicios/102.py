# Desafio 102

def calcula_fatorial(numero, show=False):
  """
    Calcula o fatorial de um número. 
    Caso o parâmetro show for True mostra o cálculo em tela.
  """
  fatorial = 1
  for c in range(numero, 1, -1):
    fatorial *= c
    if show is True:
      print(c, end=' x ')
  if show is True:
    print(1, end=' = ')
  return fatorial

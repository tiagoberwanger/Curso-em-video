#Desafio 50

def soma_numeros_pares_em_intervalo(n1, n2):
  s = 0
  for r in range(n1, n2):
    if r % 2 == 0:
      s += r
  return s
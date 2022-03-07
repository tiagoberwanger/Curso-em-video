# Desafio 47

def retorna_numeros_pares_em_intervalo(n1, n2):
  for r in range(n1, n2):
    if r % 2 == 0:
      print(r)
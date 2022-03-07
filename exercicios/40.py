# Desafio 40

from statistics import median
def calcula_media(n1, n2):
  media = median([n1, n2])
  if media < 5.0:
    return 'Reprovado'
  elif media > 5.0 and media < 6.9:
    return 'Recuperação'
  else:
    return 'Aprovado'
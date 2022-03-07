# Desafio 105

from statistics import mean

def notas(*lista_notas, sit=False):
  lista = [*lista_notas]
  maxima, media, minima, total = max(lista), mean(lista), min(lista), len(lista)
  situacao = 'BOA' if media > 7 else 'RUIM'
  retorno = { 'total': total, 'maxima': maxima, 'minima': minima, 'media': media }
  if sit is True:
    retorno['situacao'] = situacao
  return retorno
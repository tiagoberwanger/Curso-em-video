# Desafio 23

def retorna_numero_separado(numero):
  resultado = list(str(numero))
  reversed = resultado.reverse()
  for i, r in enumerate(resultado):
    if i == 0:
      print(f'unidade {r}')
    if i == 1:
      print(f'dezena {r}')
    if i == 2:
      print(f'centena {r}')
    if i == 3:
      print(f'milhar {r}')

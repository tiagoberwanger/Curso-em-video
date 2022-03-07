#Desafio 48

def retorna_numeros_impares_e_divisiveis_por_3_em_intervalo(n1, n2):
  for r in range(n1, n2):
    if r % 2 != 0 and r % 3 == 0:
      print(r)
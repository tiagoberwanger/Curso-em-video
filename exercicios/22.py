# Desafio 22

def manipula_nome(nome):
  nome_upper = nome.upper()
  nome_lower = nome.lower()
  nome_count_without_spaces = len(nome.replace(" ", ""))
  nome_count_first_name = len(nome.split(" ")[0])
  return nome_upper, nome_lower, nome_count_without_spaces, nome_count_first_name

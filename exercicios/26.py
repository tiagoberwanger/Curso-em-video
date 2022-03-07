# Desafio 26

def possui_A_no_nome(nome):
  return bool([a for a in list(nome.lower()) if a == 'a'])

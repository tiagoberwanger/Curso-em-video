# Desafio 25

def possui_silva_no_nome(nome):
  return bool([n for n in nome.split(" ") if n == "Silva"])

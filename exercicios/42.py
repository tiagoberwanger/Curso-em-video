# Desafio 42

def qual_eh_o_triangulo(l1, l2, l3):
  if l1 == l2 == l3:
    return 'Equilatero'
  elif l1 == l2 or l1 == l3 or l2 == l3:
    return 'Isósceles'
  else:
    return 'Escaleno'
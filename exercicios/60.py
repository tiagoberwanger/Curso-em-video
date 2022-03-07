#Desafio 60

def fatorial_de_um_numero(numero):
  resultado = numero
  while numero > 1:
    resultado *= (numero - 1)
    numero -= 1
  return resultado
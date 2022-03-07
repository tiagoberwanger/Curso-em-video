#Desafio 58

import random

def adivinhe_o_numero_do_computador():
  numero = random.randint(0, 10)
  tentativa = int(input('Qual é o número:'))
  x = 1

  while not tentativa == numero:
    x += 1
    tentativa = int(input('Tente novamente:'))
  
  return f'Parabéns! Você acertou após {x} tentativas'
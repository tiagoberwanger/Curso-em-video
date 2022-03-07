# Desafio 28

import random

def adivinha_numero(numero):
  numero_correto = random.randint(0, 5)
  return 'Parabéns, você acertou!' if bool(numero == numero_correto) else f'ERROU! O número é {numero_correto}'

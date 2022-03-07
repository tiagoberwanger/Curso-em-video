# Desafio 68
import random

def game_par_ou_impar():
  soma = contador = escolha = resultado = 0
  numero_pc = random.randint(1, 5)

  while escolha == resultado:
    numero = int(input('Digite um número: '))
    escolha = str(input('Digite par ou impar: '))
    print(numero_pc)
    soma = numero_pc + numero
    resultado = 'par' if soma % 2 == 0 else 'impar'
    if escolha != resultado:
      break
    contador += 1

  return f'Você ganhou {contador}x!'
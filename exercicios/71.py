#Desafio 71
#Considere que o caixa possua cédulas de R$50, R$20, R$10, e R$1
from math import floor

def simulador_caixa_eletronico():
  valor = int(input('Seja bem vindo! Deseja sacar qual valor? '))
  cedulas_50 = floor(valor / 50 if valor >= 50 else 0)
  valor -= cedulas_50*50
  cedulas_20 = floor(valor / 20 if valor >= 20 else 0)
  valor -= cedulas_20*20
  cedulas_10 = floor(valor / 10 if valor >= 10 else 0)
  valor -= cedulas_10*10
  cedulas_5 = floor(valor / 5 if valor >= 5 else 0)
  valor -= cedulas_5*5
  cedulas_1 = floor(valor / 1 if valor >= 1 else 0)
  valor -= cedulas_1*1

  c_50 = f'{cedulas_50} cédulas de R$50, ' if cedulas_50 > 0 else ''
  c_20 = f'{cedulas_20} cédulas de R$20, ' if cedulas_20 > 0 else ''
  c_10 = f'{cedulas_10} cédulas de R$10, ' if cedulas_10 > 0 else ''
  c_5 = f'{cedulas_5} cédulas de R$5, ' if cedulas_5 > 0 else ''
  c_1 = f'{cedulas_1} cédulas de R$1.' if cedulas_1 > 0 else ''

  return f'Você vai receber {c_50}{c_20}{c_10}{c_5}{c_1}'

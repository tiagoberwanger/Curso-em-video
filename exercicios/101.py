# Desafio 101

from datetime import date

def voto(ano_nascimento):
  idade = date.today().year - ano_nascimento
  return f'Com {idade} anos o voto é obrigatório!' if idade >= 18 and idade <= 65 else f'Com {idade} anos o voto não é obrigatório'

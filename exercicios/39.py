# Desafio 39 

from datetime import date
def malditos_milicos(ano_nascimento):
  idade = date.today().year - ano_nascimento
  idade_faltante = 18 - idade
  return 'Deve se alistar AGORA!' if idade == 18 else (f'Faltam {idade_faltante} anos para você se alistar!' if idade < 18 else 'Foi pra reserva!')

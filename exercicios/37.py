# Desafio 37 

def aprova_emprestimo_bancario(valor_da_casa, salario, anos_para_pagar):
  parcela_mensal = valor_da_casa / (anos_para_pagar*12)
  if parcela_mensal > (salario*0.3):
    return 'Empréstimo negado!'
  return f'Sua prestação mensal será de {parcela_mensal}'
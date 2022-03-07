# Desafio 44

def calcula_valor_total():
  parcelas = ''
  a_vista = 'a vista'
  a_prazo = 'a prazo'
  valor = int(input('Digite o valor do produto: '))
  forma_pagamento = input("Qual a forma de pagamento? (a vista, a prazo)")
  while forma_pagamento.lower() not in {a_vista, a_prazo}:
      forma_pagamento = input("Digite uma das opções: a vista / a prazo ")
  if forma_pagamento.lower() == a_prazo:
    parcelas = input("Quantas vezes? (1x, 2x, 3x - sem juros / demais 20% de juros)")
    while parcelas.lower() not in {'1x', '2x', '3x', '4x', '5x', '6x', '7x', '8x', '9x', '10x'}:
      parcelas = input("Digite uma das opções: 1x, 2x, 3x, 4x, 5x, 6x, 7x, 8x, 9x, 10x")
  return f'O valor final ficou em {(valor - valor*0.1)}' if forma_pagamento == a_vista else (f'O valor final ficou em {valor}' if parcelas == '1x' or parcelas == '2x' or parcelas == '3x' else f'O valor final ficou em {(valor + valor*0.2)}')

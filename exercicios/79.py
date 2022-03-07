# Desafio 79

def cadastra_numeros_e_ordena():
  numeros = list()
  resposta = 'S'
  while resposta in 'sS':
    numeros.append(int(input('Digite um número: ')))
    resposta = input('Quer continuar? (S/N) ')
  numeros = list(set(numeros))
  return f'Os números em ordem são {", ".join(str(n) for n in numeros)}'

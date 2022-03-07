# Desafio 82

def manipula_lista_e_imprime_pares_e_impares():
  numeros = list()
  resposta = 'S'
  while resposta in 'sS':
    numeros.append(int(input('Digite um número: ')))
    resposta = input('Quer continuar? (S/N) ')
  print(f'Os valores são {numeros}')
  print(f'Os pares são {[n for n in numeros if n % 2 == 0]}')
  print(f'Os ímpares são {[n for n in numeros if n % 2 != 0]}')

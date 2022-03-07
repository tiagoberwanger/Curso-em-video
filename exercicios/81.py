# Desafio 81

def manipula_lista():
  numeros = list()
  resposta = 'S'
  while resposta in 'sS':
    numeros.append(int(input('Digite um número: ')))
    resposta = input('Quer continuar? (S/N) ')
  print(f'Foram digitados {len(numeros)} números')
  print(f'Em ordenação decrescente fica {sorted(numeros, reverse=True)}')
  print('O valor 5 está na lista' if 5 in numeros else 'O valor 5 não está na lista')


# Listas são MUTÁVEIS, diferentemente de tuplas. Possui os métodos: append(), pop(), insert(), remove(), sort()
# Desafio 78 

def maior_e_menor_valor_de_lista():
  lista = list()
  for count in range(0, 5):
    lista.append(int(input('Digite um número: ')))
  print(f'O menor número é {min(lista)} e está na posição {lista.index(min(lista))}')
  print(f'O maior número é {max(lista)} e está na posição {lista.index(max(lista))}')

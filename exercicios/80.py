# Desafio 80

def cadastra_valores_em_ordem_crescente():
  lista = list()
  for count in range(0, 5):
    lista.append(int(input('Digite um número: ')))
  return f'Os números em ordem são {", ".join(str(n) for n in list(set(lista)))}'

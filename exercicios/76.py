# Desafio 76
listagem = ('Pão', 1.5, 'Leite', 4, 'Ovos', 8.5, 'Frango', 13)

def listagem_de_produtos(lista):
  for index in range(0, len(lista)):
    if index % 2 == 0:
      print(f'{lista[index]:.<30}', end='')
    else:
      print(f'R${lista[index]:>7.2f}')
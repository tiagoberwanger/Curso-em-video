# Desafio 91

import random

def jogo_dados():
  jogador_1 = random.randint(1, 6)
  jogador_2 = random.randint(1, 6)
  jogador_3 = random.randint(1, 6)
  jogador_4 = random.randint(1, 6)
  jogadores = dict([('jogador_1', jogador_1), ('jogador_2', jogador_2), ('jogador_3', jogador_3), ('jogador_4', jogador_4)])
  for index, jogador in enumerate(sorted(jogadores.items(), key=lambda x: x[1], reverse=True)):
    print(f'{index + 1} lugar: {jogador[0]} com {jogador[1]} pontos')

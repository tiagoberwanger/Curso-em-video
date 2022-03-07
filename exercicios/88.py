# Desafio 88

from random import randint
import time

def gerador_jogos_mega_sena(numero_jogos):
  print(f'------SORTEIO DE {numero_jogos} JOGOS------')
  for index in range(1, numero_jogos+1):
    time.sleep(1)
    lista = list()
    while len(lista) is not 6:
      r=random.randint(1,60)
      if r not in lista: lista.append(r)
    print(f'jogo {index}: {sorted(lista)}')
  print('===========BOA SORTE===========')
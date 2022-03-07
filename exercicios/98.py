# Desafio 98
import time

def contador(inicio, fim, passo):
  s = inicio
  if fim > s:
    print(s, end=' ')
    while s < fim:
      s += passo
      time.sleep(1)
      print(s, end=' ')
  print(s, end=' ')
  while s > fim:
    s += passo
    time.sleep(1)
    print(s, end=' ')
  time.sleep(1) 
  print('FIM!')
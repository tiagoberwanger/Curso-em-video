#Desafio 63

def maldito_fibonacci(numero):
  a = 0
  b = 1
  sum = 0
  while numero > 0:
    print(sum)
    a = b
    b = sum
    sum = a + b
    numero -= 1
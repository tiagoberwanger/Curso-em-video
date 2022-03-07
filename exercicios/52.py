# Desafio 52

def retorna_numero_primo(n):
  for i in range(1, n):
    return 'É primo!' if n % n == 0 and n % 1 == 0 and n % 2 != 0 and n % 3 != 0 else 'Não é primo!'

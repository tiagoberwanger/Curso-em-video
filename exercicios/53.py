# Desafio 53

def eh_palindromo(frase):
  for index, letra in enumerate(frase):
    return 'É palindromo' if frase.strip()[index] == frase.strip()[-index - 1] else 'Não é palíndromo'

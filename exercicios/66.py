#Desafio 64 / 66

def leitor_de_numeros():
  numero = 0
  soma = 0
  contador = 0
  while not numero == 999:
    numero = int(input('Digite um número para somar ou 999 para sair.'))
    if numero == 999:
      break
    soma += numero
    contador += 1

  return f'A soma é {soma} e foram digitados {contador} números'
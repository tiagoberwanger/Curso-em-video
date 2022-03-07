# Desafio 72

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

def imprime_numero_por_extenso(numeros):
  numero = int(input('Digite um número entre 0 e 10? '))
  for i, n in enumerate(numeros):
    if numero == i:
      print(f'Você digitou o número {numeros[i]}')
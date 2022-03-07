#Desafio 65

def media_minimo_maximo():
  quer_continuar = 'S'
  soma = numero = contador = media = maior = menor = 0
  while quer_continuar in 'Ss':
    numero = int(input('Digite um número'))
    soma += numero
    contador += 1
    if contador == 1:
      maior = menor = numero
    media = soma / contador
    maior = numero if numero > maior else maior
    menor = numero if numero < menor else menor
    quer_continuar = str(input('Deseja continuar? (S/N)'))
  return media, menor, maior
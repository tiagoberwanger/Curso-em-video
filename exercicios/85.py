# Desafio 85

lista = list()
pares = list()
impares = list()
for count in range(0, 7):
  numero = int(input('Digite um número: '))
  pares.append(numero) if numero % 2 == 0 else impares.append(numero)
lista.append(pares)
lista.append(impares)
numeros_pares = sorted(lista[0])
numeros_impares = sorted(lista[1])
print(f'Os números pares são {numeros_pares}')
print(f'Os números ímpares são {numeros_impares}')

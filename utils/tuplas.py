lanche = ('hamburguer', 'pastel', 'pizza', 'pudim') # A tupla é sempre IMUTÁVEL
for comida in lanche:
  print(f'Eu vou comer {comida}')
for comida in range(0, len(lanche)):
  print(f'Eu vou comer {lanche[comida]}')
for indice, comida in enumerate(lanche):
  print(f'Eu comi {comida}.')
print(f'Foram {indice+1} lanches.')
del(lanche) # É possível APAGAR uma tupla.
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = set(a + b) # Junta todos os elementos de uma tupla ignorando duplicados
print(c)
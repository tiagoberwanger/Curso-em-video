# Desafio 75
# Tupla possui dois métodos que podem ser utilizados: index() e count()

tupla = (6, 9, 9, 2, 3)

print(f'O número 3 apareceu no índice {tupla.index(3)}' if 3 in tupla else 'O número 3 não apareceu!')
print(f'O número 9 apareceu {tupla.count(9)} vezes')
print(f'Os números pares foram {", ".join([str(n) for n in tupla if n % 2 == 0])}')
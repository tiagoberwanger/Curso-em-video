# Desafio 74:

import random

numeros = tuple(str(random.randint(0, 10)) for r in range(0, 5))
numeros_formatados = " ".join(numeros)
print(f'O números sorteados foram {numeros_formatados}')
print(f'O menor é {sorted(numeros)[0]}')
print(f'O maior é {sorted(numeros)[-1]}')
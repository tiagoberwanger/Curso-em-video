# Desafio 84

pessoas = list()
pessoa = list()
resposta = 'S'
while resposta in 'sS':
  pessoa.append(str(input('Qual o nome: ')))
  pessoa.append(int(input('Qual o peso: ')))
  pessoas.append(pessoa[:])
  pessoa.clear()
  resposta = str(input('Deseja continuar? (S/N) '))

pesos = list()
for p in pessoas:
  pesos.append(p[1])

print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'A pessoa mais leve é {[p[0] for p in pessoas if p[1] == min(pesos)][0]}')
print(f'A pessoa mais pesada é {[p[0] for p in pessoas if p[1] == max(pesos)][0]}')

# Desafio 94
from statistics import mean

def cadastra_pessoas():
  pessoas = list()
  resposta = 'S'
  while resposta in 'sS':
    pessoa = dict()
    pessoa['nome'] = (str(input('Qual o nome: ')))
    pessoa['sexo'] = (str(input('Qual o sexo (M/F): ')))
    pessoa['idade'] = (int(input('Qual a idade: ')))
    pessoas.append(pessoa)
    resposta = input('Quer continuar? (S/N) ')
  numero_pessoas = len(pessoas)
  media_idade = mean([pessoa['idade'] for pessoa in pessoas])
  numero_mulheres = len([pessoa['sexo'] for pessoa in pessoas if pessoa['sexo'] == 'F'])

  return f'Foram cadastradas {numero_pessoas} pessoas. A média de idade é {media_idade} anos. Tem {numero_mulheres} mulheres.'

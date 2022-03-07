#Desafio 56

from statistics import mean

def extrator_dados(pessoas):
  media_idade_pessoas = mean([pessoa['idade'] for pessoa in pessoas]*len(pessoas))
  nome_homem_mais_velho = [pessoa['nome'] for pessoa in pessoas if pessoa['idade'] == max([pessoa['idade'] for pessoa in pessoas if pessoa['sexo'] == 'masculino'])][0]
  qtd_mulheres_menores_idade = len([pessoa['idade'] for pessoa in pessoas if pessoa['sexo'] == 'feminino' and pessoa['idade'] <= 18])
  return 'A média de idade é {} anos, o homem mais velho é o {} e há {} mulheres menores de idade'.format(media_idade_pessoas, nome_homem_mais_velho, qtd_mulheres_menores_idade)

pessoas = [{
  'nome': 'Paulo',
  'idade': 53,
  'sexo': 'masculino'  
},{
  'nome': 'Nina',
  'idade': 18,
  'sexo': 'feminino'  
},{
  'nome': 'Tiago',
  'idade': 33,
  'sexo': 'masculino'  
},{
  'nome': 'Eliza',
  'idade': 12,
  'sexo': 'feminino'
},{
  'nome': 'Daniel',
  'idade': 4,
  'sexo': 'masculino'
}]
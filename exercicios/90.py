# Desafio 90

def exibe_situacao_aluno():
  nome = str(input('Qual o nome do aluno: '))
  media = float(input('Qual a média do aluno: '))
  aluno = dict([('nome', nome), ('media', media)])
  return f'O aluno {aluno["nome"]} está aprovado' if media >= 7 else f'O aluno {aluno["nome"]} está reprovado'

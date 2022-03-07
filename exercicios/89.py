# Desafio 89

from statistics import median

def boletim_dos_alunos():
  alunos = list()
  continuar = 'S'
  while continuar in 'sS':
    aluno = list()
    notas = list()
    nome = str(input('Qual o nome do aluno? '))
    notas.append(float(input('Qual a primeira nota? ')))
    notas.append(float(input('Qual a segunda nota? ')))
    aluno.append(nome)
    aluno.append(notas)
    alunos.append(aluno)
    continuar = str(input('Quer continuar? (S/N) '))
  print('---------BOLETIM---------')
  print('NOME                MEDIA')
  for aluno in alunos:
    print(f'{aluno[0]:<20}{round(median(aluno[1]), 2)}')
  print('-------------------------')
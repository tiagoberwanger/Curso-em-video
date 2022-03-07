# Desafio 92
from datetime import date

def tempo_de_aposentadoria():
  anos_contribuicao_minima = 35
  ano_atual = date.today().year
  nome = str(input('Qual seu nome? '))
  ano_nascimento = int(input('Qual seu ano de nascimento? '))
  carteira_trabalho = int(input('Qual o número da sua carteira de trabalho? (Digite 0 se não tiver) '))
  idade = ano_atual - ano_nascimento
  dados = dict([('nome', nome), ('carteira_trabalho', carteira_trabalho), ('idade', idade)])
  if dados['carteira_trabalho'] <= 0:
    return f'{dados["nome"]}, você precisa de carteira de trabalho para se aposentar.'
  ano_contratacao = int(input('Qual foi o ano de contratação? '))
  salario = float(input('Qual seu salário? '))
  anos_contribuicao = ano_atual - ano_contratacao
  anos_para_se_aposentar = anos_contribuicao_minima - anos_contribuicao
  idade_aposentar = idade + anos_para_se_aposentar
  return f'{dados["nome"]}, você irá se aposentar com {idade_aposentar} anos.'

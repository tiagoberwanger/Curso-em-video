#Desafio 70

def leitor_de_produtos():
  soma = preco = preco_mais_barato = 0
  nome_produto = nome_mais_barato = ''
  produtos = []
  quer_continuar = 'S'

  while quer_continuar in 'Ss':
    nome_produto = str(input('Qual o nome do produto? '))
    preco = int(input('Qual o preço do produto? '))
    produtos.append(nome_produto)
    soma += preco
    if preco < preco_mais_barato or preco == 0 or preco_mais_barato == 0:
      preco_mais_barato = preco
      nome_mais_barato = nome_produto
    quer_continuar = str(input('Quer adicionar mais produtos? (S/N) '))

  return f'Os produtos adquiridos foram {produtos} e soma da sua compra é R$ {soma}. O produto mais barato foi o {nome_mais_barato}'

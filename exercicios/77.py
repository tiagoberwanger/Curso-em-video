# Desafio 77
palavras = ('tiago', 'paulo', 'nina', 'daniel')
def lista_vogais_de_palavras(palavras):
  for palavra in palavras:
    vogais = [v for v in palavra if v in ('a', 'e', 'i', 'o', 'u')]
    print(f'As vogais da palavra {palavra} são: {" ".join(vogais)}')

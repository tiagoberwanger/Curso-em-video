# Desafio 83 - NOT DONE

def gerador_de_erro_em_expressao():
  expressao = str(input('Digite a expressão: '))
  is_valid = True
  for i, l in enumerate(expressao):
    if l == '(':
      print(expressao[i])
      print(i)
      print(len(expressao))
  #     while (expressao[i] == '(' and expressao[len(expressao) - i] == ')'):
  #       is_valid = True
  #     is_valid = False
  # return is_valid

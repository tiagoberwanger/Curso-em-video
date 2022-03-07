# Desafio 31

def calcula_valor_passagem(quilometragem):
    if quilometragem <= 200:
      return f'O valor da sua passagem é R${quilometragem*0.5}'
    else:
      valor_parcial = quilometragem - 200
      return f'O valor da sua passagem é R${(200*0.5 + valor_parcial*0.45)}'

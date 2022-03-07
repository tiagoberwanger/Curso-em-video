# Desafio 43

def calcula_imc(peso, altura):
  imc = peso / (altura*altura)
  if imc < 18.5:
    return f'Seu IMC é {imc:.2f}, você está abaixo do peso'
  elif imc >= 18.5 and imc < 25:
    return f'Seu IMC é {imc:.2f}, você está peso ideal'
  elif imc >= 25 and imc < 30:
    return f'Seu IMC é {imc:.2f}, você está sobrepeso'
  elif imc >= 30 and imc < 40:
    return f'Seu IMC é {imc:.2f}, você está obesidade'
  else:
    return 'obesidade mórbida'
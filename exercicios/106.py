# Desafio 106

def pyhelp():
  funcao = ''
  while funcao != 'FIM':
    funcao = str(input('Digite um comando para ver seu manual: '))
    if funcao == 'FIM':
      break
    help(funcao)
  return 'Obrigado por usar o pyHELP'
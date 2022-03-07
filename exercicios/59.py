#Desafio 59

def calculadora():
  numero_1 = int(input('Digite o primeiro número:'))
  numero_2 = int(input('Digite o segundo número:'))
  menu = 0
  while not menu == 5:
    menu = int(input('Digite 1 para somar, 2 para multiplicar, 3 para saber o maior número, 4 para inserir novos números e 5 para sair!'))
    if menu == 1:
      print(f'A soma é {numero_1 + numero_2}')
    if menu == 2:
      print(f'O resultado da multiplicação é {numero_1 * numero_2}')
    if menu == 3:
      print(f'O maior número é {max(numero_1, numero_2)}')
    if menu == 4:
      calculadora()
  return 'Obrigado!'
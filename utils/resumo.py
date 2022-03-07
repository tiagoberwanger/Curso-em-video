from exercicios.ex110 import resumo
from exercicios.ex112 import valida_dinheiro

p = input('Digite um valor: ')
p_validado = valida_dinheiro(p)
resumo(p_validado)

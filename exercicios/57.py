#Desafio 57

def digite_seu_sexo():
    sexo = str(input('Qual seu sexo?'))
    while not (sexo == 'M' or sexo == 'F'):
        sexo = str(input('Dados inválidos, digite corretamente seu sexo (M/F)'))
    return f'Sexo {sexo} registrado com sucesso!'
# Desafio 29

def multa_se_passar_velocidade_maxima(velocidade):
    return f'Você foi multado, sua multa é de R${(velocidade - 80)*7}' if velocidade >= 80 else 'Siga em frente!'


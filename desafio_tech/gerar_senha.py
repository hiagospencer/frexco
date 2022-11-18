from random import choice
import string


def gerador_senha():
    tamanho = 8
    valores = string.ascii_lowercase + string.digits
    senha = ''
    for i in range(tamanho):
        senha += choice(valores)

    return senha

    

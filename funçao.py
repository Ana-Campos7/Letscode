
# 1 . O que são funções e por que utilizá-las?

#Funções que já utilizamos anteriormente...

"""print() # - Imprimi uma mensagem (int, float, str) no console (terminal, cmd) 

input() # - Retorna um dado informado pelo usuário (entrada padrão) e pode receber uma stric

len() # - Recebe uma lista e retorna o tamanho dessa lista #

max() # - Retorna o maior valor de una lista #"""

# Criação de Funções

# Função Inicial

def saudacao():
    print('Seja bem-vinda(o)!')
    print('Olá, é um prazer ter você fazendo parte desse curso!')

saudacao()

    # Função com parâmetros

def saudacao(nome, curso):
    print(f'Seja bem-vinda(o), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao("Ana" , "Python")
saudacao("João", "HTML")

# Função com Parâmetros default

def saudacao(nome, curso = 'Python'):
    print(f'Seja bem-vinda(o), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao("Ana")
saudacao("João", "HTML")

# Funções com retorno

def soma(num1, num2):
    return num1 + num2


resultado = (5, 7)

print('O resultado da soma é', resultado)


def calculadora(num1, num2, operacao= '+'):
    if operacao == '-':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2

resultado = calculadora(10, 20)

print(resultado)

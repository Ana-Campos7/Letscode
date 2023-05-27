
"""for variável in range(10):
    print(variável)"""


"""for variável in range(1, 10):
    print(variável)"""

# 1,4,7,10
"""for variável in range(1, 12, 3):
    print(variável)"""

"""Nota1 = float(input('Informe sua nota 1: '))
Nota2 = float(input('Informe sua nota 2: '))
Nota3 = float(input('Informe sua nota 3: '))"""

soma = 0

for i in range(1, 4):
    nota = float(input(f'Informe a sua nota{i}: '))

    soma = soma + nota

print(soma / 3)


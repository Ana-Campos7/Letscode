# > ESTRUTURAS CONDICIONAIS

idade = 20

if idade >= 18:
    print("Você é maior de idade.")
else:
    print('Você é menor de idade.')


"""
Imagine que você queira imprimir "Aprovada(O)", caso o estudante tenha uma média suprior ou igual a 7, e "Reprovada(O)", caso a média seja inferior a 7.
"""

media = float(input("Informe a média do estudante: "))
"""
if media >= 7:
    print('Você foi aprovada(o)!')
elif media >= 5:
    print('Recuperação')
else:
    print('Você foi reprovada(O).')"""    


media = 10
presenca = 50

if media >= 7 and presenca >= 70:
    print('Aprovado!')
    print('Parabéns!')
else:
    print('Reprovado')
    print('Tente novamente!')
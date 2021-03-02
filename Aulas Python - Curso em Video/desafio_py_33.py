#====DESAFIO PYTHON 33 CV ====

#Pegar o salário de uma pessoa e calcular seu aumento

salario = float(input('Informe seu salário: '))

if salario <= 1250:
    print('Seu salário de {} recebeu um aumento de 15% e ficou com R${:.2f}'.format(salario, (salario + (salario * 0.15))))

else:
    print('Seu salário de {} recebeu um aumento de 10% e ficou com R${:.2f}'.format(salario, (salario + (salario * 0.1))))
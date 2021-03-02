#====DESAFIO PYTHON 14 CV ====


funcionario_sal = float(input('Informe o seu Salário: '))

print('Salário Atual R$ {}'.format(funcionario_sal))

#Aumento de 15% no Salário
novo_salario = funcionario_sal + (funcionario_sal*0.15) #funcionario_sal + (funcionario_sal*15/100)

print('Salário com Aumento R$ {:.2f}'.format(novo_salario))



#Calculando o Salário com Imposto enviados pelo usuário
salario = int(input('Salário? '))
imposto = float(input('Imposto? '))
print('Valor real é {0}'.format(salario - (salario * imposto)))

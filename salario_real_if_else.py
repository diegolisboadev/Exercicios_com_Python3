#Calculadora para cálculo do salário real

salario = int(input('Informe seu salário? '))
imposto = input('Informe o imposto em % (ex. 27.5)? ')

if not imposto: # | imposto == '' :
    imposto = 27.5
else:
    imposto = float(imposto)

print('Valor real {0}. '.format(salario - (salario * (imposto * 0.01))))

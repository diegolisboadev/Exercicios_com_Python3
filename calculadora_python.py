
#Calculadora em Python
valor1 = float(input('Insira um Valor? '))
valor2 = float(input('Insira outro Valor? '))

operador = input('Insira um operador? +, -, *, // ')

if operador == '+' :
    resultado = valor1 + valor2
elif operador == '-' :
    resultado = valor1 - valor2
elif operador == '*' :
    resultado = valor1 * valor2
elif operador == '//' :
    resultado = valor2 // valor2
else:
    print('Erro')

print('O operador foi ' + operador +
      ' é o resultado do cálculo é: {0}'.format(resultado))
                    
                    

>>> valor1 = int(input('Insira um valor? '))
Insira um valor? 4
>>> valor2 = int(input('Insira outro valor? '))
Insira outro valor? 3
>>> print(valor1 + valor2)
7
>>> print(valor * valor2)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(valor * valor2)
NameError: name 'valor' is not defined
>>> print(valor1 * valor2)
12
>>> print(valor1 // valor2)
1
>>> print(valor1 / valor2)
1.3333333333333333
>>> print(valor1 ** valor2)
64
>>> print(valor1 *** valor2)
SyntaxError: invalid syntax
>>> imposto = o.27
SyntaxError: invalid syntax
>>> imposto = 0.27
>>> salario = 5000
>>> print(salario - (salario * imposto))
3650.0
>>> print('Valor real: {0}'.format(salario - (salario * imposto)))
Valor real: 3650.0
>>> imposto = float(input('Insira o valor do Imposto: '))
Insira o valor do Imposto: 0.27
>>> salario = int(input('Insira o seu salãrio?'))
Insira o seu salãrio?3000
>>> print('O valor com o imposto é {0}:'.format(salario - (salario * imposto)))
O valor com o imposto é 2190.0:
>>> 
== RESTART: C:/Users/Diego Lisboa/Downloads/Aulas Python 3/salario_real.py ==
Salário? 3000
Imposto? 0.27
Valor real é 2190.0
>>> 1 >= 1
True
>>> 2 < 1
False
>>> 9 == 9
True
>>> 9 != 8
True
>>> 2 <= 3
True
>>> 1 == 1.0
True
>>> 10 > 1j
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    10 > 1j
TypeError: '>' not supported between instances of 'int' and 'complex'
>>> exit()
>>> 

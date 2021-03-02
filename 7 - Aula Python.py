#Função em Python
>>> def soma(a, b):
	print(a + b)

>>> c = soma(1, 2)
3

>>> def soma(a, b):
	return a + b
c = soma(3,1)

>>> print(c)
4

>>> def salario_descontado_imposto(salario, imposto = 27.):
	return salario - (salario * imposto * 0.01)

>>> salario_descontado_imposto(5000)
3650.0

>>> #Parametros Nomeados - mudando o valor padrão do argumento
>>> salario_descontado_imposto(5000, imposto=0.10)
4995.0

>>> salario_descontado_imposto(5000, imposto=0.10)
4995.0

>>> #Packing e Unpacking - Números arbitrários de argumentos
>>> from datetime import date
>>> d = (2018, 1, 14)
>>> date(d[0], d[1], d[2])
datetime.date(2018, 1, 14)
>>> #Usando o Packing para uma lista ou tupla
>>> from datetime import date
>>> d = (2018, 1, 14)
>>> date(*d)

>>> #Importação de modulos e objetos
	  
>>> import math
	  
>>> print(math.sqrt(9))
	  
3.0
>>> import math as matematica
	  
>>> print(matematica.sqrt(9))
	  
3.0
>>> #Importanto uma objeto de um módulo
	  
>>> from unittest import TestCase
	  
>>> from math import log2 as 12
	  
SyntaxError: invalid syntax
>>> from math import log2 as l2
	  
>>> print(l2(1024))
	  
10.0
>>> for i in range(10):
	  print(i)

	  
0
1
2
3
4
5
6
7
8
9
>>> 

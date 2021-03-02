>>> #Listas em Python

>>> [1,2,3,4,5]
[1, 2, 3, 4, 5]
>>> ['salário', 'imposto']
['salário', 'imposto']
>>> [1, 'salario']
[1, 'salario']
>>> [[1,2,3], 'salario', 10]
[[1, 2, 3], 'salario', 10]
>>> lista = ['imposto', 'salário', 'altos', 'baixos']
>>> lista[0]
'imposto'
>>> lista[3]
'baixos'
>>> lista[2:3]
['altos']
>>> lista[1:3]
['salário', 'altos']
>>> lista[0:2]
['imposto', 'salário']

>>> #Listas são mutáveis - modificando a posiçao pegando o indice
>>> lista[2] = 'Altos'
>>> print(lista)
['imposto', 'salário', 'Altos', 'baixos']
>>> lista[3] = 'dinheiro'
>>> print(lista)
['imposto', 'salário', 'Altos', 'dinheiro']
>>> lista[0:2] = ['Impostos', 'Salários']
>>> lista
['Impostos', 'Salários', 'Altos', 'dinheiro']

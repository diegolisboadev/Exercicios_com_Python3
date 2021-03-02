#Aula 02 de Python

>>> #Manipulando strings em Python
>>> #coding utf-8
>>> "Copa 2018"
'Copa 2018'
>>> 'Copa do Mundo'
'Copa do Mundo'
>>> ´Copa do Mundo'
SyntaxError: invalid character in identifier
>>> '''2018 - Copa do Mundo '''
'2018 - Copa do Mundo '
>>> "copa 'padrão Fifa'"
"copa 'padrão Fifa'"
>>> 'copa "padrão fica"'
'copa "padrão fica"'
>>> #Multiline Strings

#A barra corresponde à um \n para espaçamento
>>> print("""\
	  Uso: consulta_base [OPCOES]
		  -h
		  -U url
	""")
	  Uso: consulta_base [OPCOES]
		  -h
		  -U url
	
>>> print("Copa" "2014")
Copa2014
>>> 'Copa' '\' 'Mundo'
SyntaxError: invalid syntax
>>> print('Copa', '\ Mundo')
Copa \ Mundo
>>> input('Em qual cidade o legado da Copa foi mais relevante'				'para a população?')
Em qual cidade o legado da Copa foi mais relevantepara a população?
''
>>> input('Em qual cidade o legado da copa foi mais relevante'					'para a população?')
Em qual cidade o legado da copa foi mais relevantepara a população?
''

#Ligando duas strings com tab
>>> input('Em qual cidade o legado da copa foi mais relevante '					'para a população?')
Em qual cidade o legado da copa foi mais relevante para a população?
''
>>>
#u - era usado na versão 2 do Python para dizer que o encode é utf-8
>>> print(u'minha string')
minha string
>>> print('minha string')
minha string
>>> u'olá'
'olá'
>>> 'olá'
'olá'
>>> variavel['olá']
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    variavel['olá']
NameError: name 'variavel' is not defined
>>> 'Python'
'Python'
>>> variavel[1]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    variavel[1]
NameError: name 'variavel' is not defined
>>> 'Python'
'Python'

#len() tamanho da string
>>> len('Python')
6
>>> len('Hello World!!')
13
>>> string = 'Diego'

#Verificar uma letra pela posição no array
>>> string[1]
'i'
>>> string[5]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    string[5]
IndexError: string index out of range
>>> string[4]
'o'

#Verificando a posição de uma letra por trechos
>>> string[1:3]
'ie'
>>> string[2:4]
'eg'
>>> st = 'maracana'
>>> st[0]
'm'
>>> st[1:4]
'ara'
>>> st[2:]
'racana'
>>> st[:3]
'mar'
>>> len(str)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    len(str)
TypeError: object of type 'type' has no len()
>>> len(st)
8

#Procurando a existência de um elemento em uma string
>>> 'm' in 'maracana'
True
>>> 'a' in 'maracana'
True
>>> 'e' in 'maracana'
False

#Verificando se uma string mão está na string
>>> 'x' not in 'chuva'
True
>>> 'c' not in 'chuva'
False
>>> 'm' in 'maracana'
True
>>> 'x' not in 'maracana'
True

#Concatenando strings (adicionando uma string a outra)
>>> 'm' + 'aracana'
'maracana'

#Repetindo uma string
>>> 'a' * 3
'aaa'
>>> 'm' ** 4
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    'm' ** 4
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> 'm' * 5
'mmmmm'
>>> 3 * 'b'
'bbb'
>>> 
>>> minha_str = 'livro python 3'
>>> minha_str[13] = '2'
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    minha_str[13] = '2'
TypeError: 'str' object does not support item assignment
>>> minha_str[2] = '2'
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    minha_str[2] = '2'
TypeError: 'str' object does not support item assignment

#Concatenando uma string com outra
#pegando a posição por trechos 
>>> minha_str = 'livro_python 3'
>>> minha_str = minha_str[0:13] + '2'
>>> print(minha_str)
livro_python 2

#Substituindo uma string por outra replace()
>>> minha_str = 'livro_python 4'
>>> minha_str = minha_str.replace('3','2')
>>> print(minha_str)
livro_python 4
>>> minha_str = minha_str.replace('4','2')
>>> print(minha_str)
livro_python 2
>>> 
>>> frase = 'Diego 2019'
>>> frase = frase[1:5] + '25'
>>> print(frase)
iego25
>>> frase = frase.replace('25', '')
>>> print(frase)
iego
>>> frase = 'nome:'
>>> frase2 = 'Diego'
>>> frase_final = join(frase, frase2)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    frase_final = join(frase, frase2)
NameError: name 'join' is not defined
>>> frase = frase.join(frase, frase2)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    frase = frase.join(frase, frase2)
TypeError: join() takes exactly one argument (2 given)
>>> frase = frase.capitalize(frase, frase2)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    frase = frase.capitalize(frase, frase2)
TypeError: capitalize() takes no arguments (2 given)

#Frase com Inicial maiscula
>>> frase = frase.capitalize()
>>> print(frase)
Nome:
>>> frase = 'maracana'
>>> print(frase)
maracana

#Contando uma string
>>> 'maracana'.count('r')
1
>>> 'maracana'.count()
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    'maracana'.count()
TypeError: count() takes at least 1 argument (0 given)
>>> 'maracana'.endswith('brasil')
False
>>> 'maracana'.end
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    'maracana'.end
AttributeError: 'str' object has no attribute 'end'

#Verificando o último elemento de uma string
>>> 'maracana'.endswith('a')
True

#Verificando o elemento inicial de uma string
>>> 'maracana'.starswith('m')
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    'maracana'.starswith('m')
AttributeError: 'str' object has no attribute 'starswith'
>>> 'maracana'.startswith('m')
True
>>> 'maracana'.startswith('a')
False
>>> 'copa de 2014'.split('')
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    'copa de 2014'.split('')
ValueError: empty separator

#Verificando o elemento separador de uma string
>>> 'copa de 2018'.split(' ')
['copa', 'de', '2018']
>>> 'copa, de, 2018'.split(',')
['copa', ' de', ' 2018']
>>> ' '.joint(['copa', 'de', '2018'])
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    ' '.joint(['copa', 'de', '2018'])
AttributeError: 'str' object has no attribute 'joint'
>>> ' ',join(['copa', 'de', '2018'])
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    ' ',join(['copa', 'de', '2018'])
NameError: name 'join' is not defined
>>> 'copa de 2018'.split(' ')
['copa', 'de', '2018']

#Definindo um elemento separador para string
>>> ''.join(['copa', 'de', '2018'])
'copade2018'
>>> 'copa de 2018'.replace('2018', '2014')
'copa de 2014'
>>> #Formatando strings
>>> '%d para a copa' % (100)
'100 para a copa'
>>> '%s tudo bom!!' % ('Diego')
'Diego tudo bom!!'
>>> '{} dias para a copa'.format(100)
'100 dias para a copa'
>>> '{dias} para a copa'.format(dias = 100)
'100 para a copa'
>>> #Espaçamentos e alinhamentos
>>> '{:<60}'.format('alinhado à esquerda ocupando 60 posições')
'alinhado à esquerda ocupando 60 posições                    '
>>> '{:>60}'.format('alinhado à direita ocupando 60 posições')
'                     alinhado à direita ocupando 60 posições'
>>> '{:^60}'.format('centralizado ocupando 60 posições')
'             centralizado ocupando 60 posições              '
>>> '{:.^60}'.format('centralizado ao alterar caractere de espaçamento')
'......centralizado ao alterar caractere de espaçamento......'

#Mais sobre a manipulação de STRINGS em Python

>>> " 'Olá, tudo bem?' "
" 'Olá, tudo bem?' "
>>> ' ´como foi '
' ´como foi '
>>> "The 'PYTHON' "
"The 'PYTHON' "
>>> string = 'ola'
>>> print(string)
ola

#Deixando as Primeiras letras de cada palavra Maiusculas title()
>>> print(string.title())
Ola

#Verificando se a palavra e toda minuscula
>>> print(string.islower())
True

#Verificando se a palavra e toda maiuscula
>>> print(string.isupper())
False
>>> name = 'ada lovelace'
>>> name.title()
'Ada Lovelace'
>>> name.capitalize()
'Ada lovelace'

#Deixando a palavra minuscula
>>> name.lower()
'ada lovelace'

#Deixando a palavra maiuscula
>>> name.upper()
'ADA LOVELACE'

#Concatenando Strings +
>>> first_name = 'ada'
>>> last_name = 'lovelace'

>>> print(first_name + last_name)
adalovelace
>>> print(first_name + ' ' + last_name)
ada lovelace
>>> full_name = first_name + ' ' + last_name

#Imprimindo String Formatada com + e title()
>>> print(full_name.title() + '!')
Ada Lovelace!

#Usando \t para tabulação (tab)
>>> print('\tPython')
	Python

#Usando o \n para quebra de linha (<br>)
>>> print('Python\n')
Python

>>> print('\nPython')

Python
>>> print('\n\tPython \n\tPHP \n\tJava')

	Python
	PHP
	Java
>>> print('\n\tPython \n\t\tPHP \n\t\t\tJava')

	Python
		PHP
			Java

#Utilziando rstrip() para remover espaços em branco à direita
>>> favorite_l = 'python '
>>> favorite_l.rstrip()
'python'
>>> favorite_l = ' python'

#Utilizando lstrip() para remover espaços em branco à esquerda
>>> favorite_l.lstrip()
'python'
>>> favorite_l
' python'
>>> favorite_l = favorite_l.lstrip()
>>> favorite_l
'python'
>>> favorite = 'python '
>>> favorite = favorite.rstrip()
>>> favorite
'python'
>>> favorite = ' python '

#Utilizando strip() para remover espaços em branco de ambos os lados
>>> favorite = favorite.strip()
>>> favorite
'python'
>>> 'python ´ficou só´
SyntaxError: EOL while scanning string literal

#Imprimindo corretamente uma string com " ' "
>>> "Um Python's é forte"
"Um Python's é forte"

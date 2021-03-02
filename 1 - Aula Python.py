//Inserindo Valores Python
>>> 1
1

//Divisão de Valores com retorno float()
>>> 3 / 2
1.5

//Olá Mundo!! em Python
>>> print('Hello World', '\n', 'Diego')
Hello World 
 Diego

//Usuário inserindo o nome e depois mostrando na tela
>>> nome = input('Insira seu Nome')
Insira seu Nome Diego Lisboa
>>> print('Olá', nome)
Olá  Diego Lisboa

//Números Complexos  
>>> complex(10)
	 
(10+0j)
>>> complex(-10)
	 
(-10+0j)

//Fim dos Números Complexos

//Inteiro valores
>>> int('1')
	 
1

//Pontos (números) flutuantes recebendo string
>>> float('+nan')
	 
nan

//Números Complexos
>>> complex(1+2j.real)
	 
(1+0j)
>>> complex(1+2j.imag)
	 
(3+0j)

//Fim Numeros Complexos

//int()
>>> 1
	 
1

float()
>>> 1.0
	 
1.0

complex()
>>> 1+2j
	 
(1+2j)

complex() retornando o valor real
>>> 1+2j.real
	 
1.0
>>> 1+2j.imag
	 
3.0

//Fim complex() retornando o valor real

>>> int(1.0)
	 
1
>>> int('9')
	 
9
>>> float(1)
	 
1.0
>>> float('9.2')
	 
9.2
>>> float('+inf')
	 
inf
>>> float('nan')
	 
nan
>>> float('-inf')
	 
-inf
>>> complex(1,2)
	 
(1+2j)
>>> 3+2
	 
5
>>> soma = int(3+2)
	 
>>> print(soma)
	 
5
>>> 3+4.2
	 
7.2
>>> 4 / 2
	 
2.0
>>> 5 / 2
	 
2.5

//Divisão de valor com retorno inteiro
>>> 5 // 2
	 
2

//Testes com Números Complexos
>>> complex(1,2) + 2
	 
(3+2j)
>>> complex(2,0) + 0+1j
	 
(2+1j)
>>> complex(2,1) + 0+3j
	 
(2+4j)
>>> complex(2,1) + 2+2j
	 
(4+3j)
>>> complex(2,1) + (2+2j)
	 
(4+3j)
>>> 2 + 0+1j
	 
(2+1j)

//Fim Testes com Números Complexos

//Expoenciação com Python
>>> 3 ** 2
	 
9
>>> 1 + 2
	 
3
>>> 3-1
	 
2

//Divisão com resultado fracionário
>>> 10/2
	 
5.0

//Divisão com resultado inteiro
>>> 10//2
	 
5
>>> 10 * 2 + 1
	 
21

//Divisão mostrando o resto como resultado
>>> 10 % 3
	 
1
>>> -3
	 
-3
>>> 2 ** 8
	 
256

//Operadores de lógicos

//Ou |
>>> 1 | 0
	 
1
>>> 0 | 1
	 
1
>>> 2 | 2
	 
2
>>> 3 | 2
	 
3
>>> 1 | 5
	 
5

//OU Exclusivo
>>> 1 ^5
	 
4
>>> 5 ^1
	 
4
>>> 1^1
	 
0
>>> 2^1
	 
3

//E
>>> 4 & 1
	 
0
>>> 3 & 3
	 
3
>>> 1 & 3
	 
1

//X com Y bits deslocados à esquerda
//Bits à esquerda 16
>>> 4 << 2
	 
16
>>> 1 << 2
	 
4

//X com Y bits deslocados à direita
//Bits à direita 0
>>> 2 >> 2
	 
0
>>> 2 >> 1
	 
1
>>> 5 >> 3
	 
0

//Inverso em Bits
//Inverso -5 
>>> ~4
	 
-5
>>> ~2
	 
-3
>>> ~1
	 
-2
>>> ~8
	 
-9
>>> 100 * 1.3
	 
130.0
>>> float(100 * 1.3)
	 
130.0

//Função para type() - define o tipo do dado inserido
>>> type(1)
	 
<class 'int'>
>>> type(2.9)
	 
<class 'float'>
>>> type(1+2.0)
	 
<class 'float'>

#Comentário em Python #

>>> type(1+2j)
	 
<class 'complex'>
>>> type(1.0+2j)
	 
<class 'complex'>
>>> type(1.0+1.0)
	 
<class 'float'>
>>> 

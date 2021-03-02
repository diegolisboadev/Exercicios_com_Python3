#==== Aula 07 Operadores Aritméticos

# + - * / ** // %

#Ordem de Precedência dos Operadores Aritméticos em Python

# 1 - ()
# 2 - **
# 3 - * / // %
# 4 - + -

expre1 = 5 + 3 * 2

print(expre1)

expre2 = 3*5+4**2
print(expre2)

expre3 = 3*(5+4)**2
print(expre3)

#Calcula também a potência, porém sem precedência

pow(4,2)

#Modo de tirar a raiz quadrada e cúbica
print(81**(1/2))

print(25**(1/2))

print(127**(1/3))

#Utilizando Operadores com Strings

print('oi'*5)

print('='*20)

nome = input('Qual o seu nome? ')

#20 campos de caractere
print('Prazer em te conhecer {:20}!'.format(nome))

#20 caracteres alinhados à direita do nome
print('Prazer em te conhecer {:>20}!'.format(nome))

#20 caracteres alinhados à esquerda do nome
print('Prazer em te conhecer {:<20}!'.format(nome))

#Deixando o nome centralizado entre 20 espaços à esquerda e à direita
print('Prazer em te conhecer {:^20}!'.format(nome))

#Deixando o nome centralizado entre 20 espaços à esquerda e à direita com o sinal de =
print('Prazer em te conhecer {:=^20}!'.format(nome))


#Calculadora - Testando os operadores Aritméticos

n1 = int(input('Digite um valor? '))
n2 = int(input('Outro valor? '))

e = n1**n2
m = n1*n2
df = n1/n2
di = n1//n2
s = n1+n2
sub = n1-n2

print('A exponenciação é {} \n a multiplicação é {} \n a divisão-float é {:.3f} \n '
      'a divisão-int é {} \n a subtração é {} \n a soma é {} !'.format(e,m,df,di,sub,s), end=' ')

#Obs. o end= significa a exclusão da quebra de linha, colocando uma string a outra ou print a outro
#definindo um elemento após o fim da string

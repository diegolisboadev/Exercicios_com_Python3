
#====DESAFIO PYTHON 21 CV ====

#Utilizando algumas funções de strings Python

nome = input('Insira seu nome Completo: ')

#Forma abaixo eliminar os espaços antes e depois da string diretamente
#nome = str(input('Insira seu nome Completo: ')).strip()

print("Nome maiusculo {}".format(nome.upper()))

print('Nome minusculo {}'.format(nome.lower()))

#Contar todas letras sem contar os espaços

#Primeiro forma que eu encontrei não correta porém resolveu o problema kk

#nomes = nome.split()
#tam_nomes = nomes[0]+nomes[1]+nomes[2]

#print('Tamanho do Nome tirandos os espaços {0}{1}{2}, '
      #'com o tamanho de {3} caracteres'.format(nomes[0], nomes[1], nomes[2], len(tam_nomes)))

#Segunda forma que achei mais coerente kkk

print('O tamanho do seu nome em sem os espaços é {} caracteres'.format(len(''.join(nome.split()))))
#len(nome) - nome.count(' ') #Outra forma de elimar os espaços entre strings

#Quantas letras tem o primeiro nome

conta = nome.split()

print('O seu primeiro nome tem {} caracteres'.format(len(conta[0])))

#nome.find(' ') #Encontra o primeiro espaço na string e mostra o conteudo nos indices ate
#o próximo espaço
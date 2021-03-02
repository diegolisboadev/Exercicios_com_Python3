
#====DESAFIO PYTHON 16 CV ====

#Realizando o cálculo do Triângulo Retângulo

#h^2 = a^2 + b^2

from math import hypot, sqrt

cateto_oposto = float(input("Insira o Cateto Oposto: "))
cateto_adjacente = float(input('Insira o Cateto Adjacente: '))

#Calculando a hipotenusa usando a função hypot
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

#Calculando a Hipotenusa manalmente
#hipo = pow(cateto_oposto, 2) + pow(cateto_adjacente, 2)
#hipotenusa = sqrt(hipo)
#Outra solução
#hipotenusa = (cateto_oposto**2 + cateto_adjacente**2) ** (1/2)

print('A Soma do Quadrado do Cateto Oposto {} + do Cateto Adjacente {}'
      ' tem a Hipotenusa {:.2f}'.format(cateto_oposto, cateto_adjacente, hipotenusa))


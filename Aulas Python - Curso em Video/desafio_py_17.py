
#====DESAFIO PYTHON 17 CV ====

#Mostrando o Seno, Cosseno, Tangente de um Ângulo

from math import sin, cos, tan, radians

angulo = float(input('Informe um ângulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))


print('O Seno de {} é {:.2f} \n O Cosseno é {:.2f} \n A Tangente é {:.2f}'
      .format(angulo, seno, cosseno, tangente))
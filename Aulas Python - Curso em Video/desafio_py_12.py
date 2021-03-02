#====DESAFIO PYTHON 12 CV ====

#Faça um programa que leia a largura e a altura de uma parede
#de uma parede em metros, calcule a sua área e a quantidade de tinta
#necessária para pintá-la, sabendo que cada litro de tinta, pinta uma
#área de 2m^2.

largura = float(input('Insira a Largura da Parede (m): '))
altura = float(input('Insira a Altura da Parede (m): '))

#Calculo da Área
area = (largura*altura)

print('Área {} m^2'.format(area))

#Quantidade de Tinta necessária para pintar essa parede

tinta_area = area/2

print("A quantidade de tinta para pintar a parede é de {} L".format(tinta_area))


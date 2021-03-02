
#====DESAFIO PYTHON 14 CV ====

#Tranformando de Cº para Fº

graus_c = float(input('Informe os Cº: '))

print('A temperatura de {}Cº corresponde à {:.1f}Fº'.format(graus_c, ((9/5) * graus_c + 32)))

#Tranformando de Fº para Cº

farenheint = float(input('Informe Fº: '))

print('A temperatura de {}Fº corresponde à {:.1f}Cº'.format(farenheint, ((farenheint - 32) * 5/9)))
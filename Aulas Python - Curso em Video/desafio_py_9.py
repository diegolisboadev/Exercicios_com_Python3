#====DESAFIO PYTHON 9 CV ====

#Mostrando algumas conversões de metro para km, hm, dam, dm, cm, mm

valor = float(input('Insira um valor em metros: '))

#cent = valor*100
#mil = valor*1000

print('O {} corresponde \n'
      'Em Kilometros à {} km \n'
      'Em Hectometro à {} hm \n'
      'Em Decâmetro {} dam \n'
      'Em Decimetro {} dm \n'
      'Em Centimetro {:.0f} cm \n' #Exercicio
      'Em Milimetro {:.0f} mm' #Exercicio
      .format(valor, valor/1000, valor/100, valor/10, valor*10, valor*100, valor*1000))
#====DESAFIO PYTHON 30 CV ====

#Calcular o preço a ser pago pela distancia da viagem menor que 200km e maior que 200km

from time import sleep

distancia = float(input('Informe a distância de sua viagem (KM): '))

print('Calculando o preço da passagem...')
sleep(5)

#Obs. grandes comentários em python ''' ''' (três aspas simples)
'''if distancia <= 200:
    print('O preço da passagem até {}Km é R${:.2f}'.format(distancia, (distancia * 0.50)))
else:
    print('O preço da passagem pelos {}Km é R${:.2f}'.format(distancia, (distancia * 0.45)))'''

#Condição simplificada
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print('O preço de sua passagem será de {}'.format(preco))
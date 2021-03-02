#====DESAFIO PYTHON 28 CV ====

#Lendo a velocidade de um carro, verificando se ele foi multado e mostrando o valor da multa

from time import sleep

km = float(input('Informe a velocidade do Carro: '))

print('Processando...')
sleep(5)

if km > 80:

    print('Ei você acabou de ser multado, por excesso de velocidade')
    print('O valor da multa acima do limite é de R${:.2f}'.format((km - 80) * 7))

print('Você está trafegando na velocidade de {} Km!! Boa viagem!!'.format(km))
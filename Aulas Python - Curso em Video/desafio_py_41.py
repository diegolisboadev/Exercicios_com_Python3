
#====DESAFIO PYTHON 41 CV ====

#Verificando se gerar um triângulo, se sim ele é equilatero, isósceles ou escaleno
from time import sleep

retas = []

for r in range(0,3):
    linhas = float(input('Informe a reta {}: '.format(r)))
    retas.append(linhas)

print('Verificando...')
sleep(2)

if retas[0] + retas[1] > retas[2] \
    and retas[0] + retas[2] > retas[1] \
    and retas[2] + retas[1] > retas[0]:
    print('Forma um triângulo de {:.0f} lados'.format(sum(retas)))

    if retas[0] == retas[1] == retas[2]:
        print('Triângulo Equilátero')

    elif retas[0] == retas[1] or retas[1] == retas[2] or retas[2] == retas[0]:
        print('Triângulo Isósceles')

    else: #retas[0] != retas[1] != retas[2] != retas[1]:
        print('Triângulo Escaleno')

else:
    print('Não forma um triângulo!!!')
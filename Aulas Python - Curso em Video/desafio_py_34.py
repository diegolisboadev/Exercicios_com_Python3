#====DESAFIO PYTHON 34 CV ====

#Pegar 3 retas e dizer se elas formam um triângulo
#Se a soma de dois lados for maior que o 3 lado então o triângulo existe
#se não triângulo não existe

from time import sleep

retas = []

for reta in range(0,3):
    linhas = float(input('Informe a reta: '))
    retas.append(linhas)

#Verificando
print('Verificando...')
sleep(5)

if (retas[0] + retas[1]) > retas[2] and (retas[0] + retas[2]) > retas[1] and (retas[2] + retas[1]) > retas[0]:
    print('Forma um triângulo de {:.0f} lados'.format(sum(retas)))
else:
    print('Não forma um triângulo!!!')


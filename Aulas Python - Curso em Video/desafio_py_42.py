
#====DESAFIO PYTHON 42 CV ====

#Calcula IMC e mostrar resultado

peso = float(input('Informe seu peso (Kg): '))
altura = float(input('Informe sua altura (m): '))

imc = peso / pow(altura, 2) #(altura ** 2)

resultado = None

if imc < 18.5:
    resultado = '\033[1;30;41m ABAIXO DO PESO \033[0;m'

elif 18.5 <= imc < 25:
    resultado = '\033[1;30;44m PESO IDEAL \033[0;m'

elif 25 <= imc < 30:
    resultado = '\033[1;30;45m SOBREPESO \033[0;m'

elif 30 <= imc < 40:
    resultado = '\033[1;30;43 OBESIDADE \033[0;m'

else:
    resultado = '\033[1;30;41m OBESIDADE MÓRBIDA \033[0;m'

print('Você tem o peso de {} e a altura {}, seu IMC é {:.2f}'.format(peso, altura, imc))
print('Você está com {}'.format(resultado))


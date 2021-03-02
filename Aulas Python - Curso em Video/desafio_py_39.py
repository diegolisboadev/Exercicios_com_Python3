#====DESAFIO PYTHON 39 CV ====

#Ler duas notas de uma aluno e calcular sua média

nota1 = float(input('Informe a sua primeira nota: '))
nota2 = float(input('Informe a sua segunda nota: '))

media = (nota1 + nota2) / 2

resultado = 0

if media < 5.0:
    resultado = 'REPROVADO'

elif 6.9 >= media >= 5.0:
    resultado = 'RECUPERAÇÃO'

elif media >= 7.0:
    resultado = 'APROVADO'

print('A sua média é {:.1f} e seu resultado final foi {}'.format(media, resultado))



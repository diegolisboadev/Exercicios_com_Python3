#====DESAFIO PYTHON 25 CV ====

#

frase = str(input('Informe uma frase qualquer: ')).strip()

#Quantas vezes aparece a letra 'a' ou 'A'
print('O a aparece {} vezes'.format(frase.lower().count('a')))

#Em que posição o 'a' ou 'A' aparece a primeira vez na frase
print('O a aparece a primeira vez na posição {}'.format(frase.lower().find('a')))

#Em que posição o 'a' ou 'A' aparece a ultima vez na frase
#Obs. o metodo rfind() procurar a string da direita para a esquerda

print('O a aparece a última vez na posição {}'.format(frase.lower().rfind('a')))
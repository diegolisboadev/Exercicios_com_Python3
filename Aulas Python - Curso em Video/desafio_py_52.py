
#====DESAFIO PYTHON 52 CV ====

#Ler uma frase e verificar se é um PALINDROMO (Mesma coisa de trás pra frente)

frase = str(input('Diga a frase: ')).strip().split()

frase = ''.join(frase)

#Fatiando a String de Trás pra Frente
fras = frase[::-1]

if frase == fras:
    print('''A frase \033[0;33m{}\033[m é igual a
    \033[0;33m{}\033[m de trás para frente (PALINDROMO)'''.format(frase, fras))
else:
    print('''A frase \033[0;33m{}\033[m é diferente da
    \033[0;33m{}\033[m de trás para frente (NÃO PALINDROMO)'''.format(frase, fras))
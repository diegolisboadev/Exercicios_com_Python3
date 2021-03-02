
#====DESAFIO PYTHON 46 CV ====

#Todos os numeros pares no intervalo entre 1 e 50

for n in range(1, 51): #Ou de 2 em 2 (range(2, 50, 2))
    if n % 2 == 0:
        print(n, end=' ')
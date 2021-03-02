#Laço While - Curso em Video

n = 1
par = impar = 0

while n != 0:
    n = int(input("Digite um número: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("Você digitou {} numeros pares e {} impares".format(par, impar))


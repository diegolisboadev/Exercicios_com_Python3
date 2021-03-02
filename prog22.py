
#Programa 22 Curso Intensivo Python

#exerc 22

print('='*20)

#Lista de 1 a 20
for value in range(1,21):
    print(value)

print('='*20)

#Lista de 1 a 1 milhão
#lista = list(range(1, 1000001))

#for l in lista:
    #print(l)

print('='*20)

#Lista de 1 a 1 milhão com detalhes de menor valor, maior valor e soma da lista
lista2 = list(range(1,1000001))

#print('Minimo valor da lista 1 a 1 milhão {}'.format(min(lista2)))
#print('Maximo valor da lista de 1 a 1 milhão {}'.format(max(lista2)))
#print('Soma desses valores {}'.format(sum(lista2)))

print('='*20)

#Numeros Impares de 1 a 20
num_impar = list(range(1,21,2))

for impar in num_impar:
    print(impar)

print('='*20)

#Lista de números de múltiplos de 3, de 3 a 30

mult3 = list(range(3,30,3))

for mult in mult3:
    print(mult)

print('='*20)

#Cubo de 1 a 10

cubos = []

for cub in range(1,11):
    cubos.append(pow(cub, 3))

print(cubos)

print('='*20)

#Usando list comprenshions para mostrar o cubo de 1 a 10

cubo = [pow(cb, 3) for cb in range(1,11)]
print(cubo)

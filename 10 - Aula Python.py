#Tuplas são imutaveis, ou seja, não podem mudar, porém listas são mutáveis
#É recomendado usar tuplas para dados que não serão alterados durante a vida
#útil de um programa

dimen = (200, 50) #Tupla usa () já lista usa []

print(dimen[0])
print(dimen[1])

#dimen[0] = 100 Não permitido pois uma tupla é imutavel, ou seja, seus valores não mudam
#print(dimen[0])

#Percorrendo uma tupla com o laço for

for d in dimen:
    print(d)

#Sobrescrevendo uma tupla
dime = (200, 50)
print('Tupla Original {}'.format(dimen))

#Tupla sobrescrita
dime = (400, 100)
print('Tupla modificada {}'.format(dime))
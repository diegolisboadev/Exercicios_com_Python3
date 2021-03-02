#Iniciando desafio 1

#Imprimindo o nome do usuário direto do input
'''print('====DESAFIO 1====')
nome  = input('Informe seu nome ')
print('Olá', nome, 'prazer em conhecê-lo!!')'''


#Veriricar esse código - inserir uma lista e somar os dados da lista

num = []

#num = input('Número: ').split()

for l in range(5):
    ls = int(input('Informe um número: '))
    num.append(ls)

#Prita lista
print(num)
#Soma Lista
print(sum(num))

#Somatório de Lista Dinâmica
nume = []

flag = ''

while flag != 0:
    flag = int(input('Informe um número: '))
    nume.append(flag)

    if(flag == 0):
        r = str(input("Deseja Sair? [s]/[n]"))

        if(r == 's'.lower()):
            exit(-1)

print(nume)
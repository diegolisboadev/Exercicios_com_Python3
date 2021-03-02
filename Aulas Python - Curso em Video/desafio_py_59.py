
#====DESAFIO PYTHON 59 CV ====

#Fatorial de um número

fatorial = int(input("Digite um número: "))
num_fat = fatorial
calc = 1

#Com While
while fatorial != 0:
    print("{} x {} = {}".format(calc, fatorial, (calc * fatorial)))
    calc *= fatorial
    fatorial -= 1
print("O Fatorial de {} é {}".format(num_fat, calc))

#Com For
'''for fat in range(fatorial, -1, -1):
    print("{} x {} = {}".format(calc, fat, (calc * fat)))
    calc = calc * fat
print("O Fatorial de {} é {}".format(num_fat, calc))'''

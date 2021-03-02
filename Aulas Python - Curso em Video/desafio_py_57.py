
#====DESAFIO PYTHON 57 CV ====

#Tente adivinhar o número que o computador pensou, testando as possibilidades

from random import randint

print("=="*10)
print("Advinhe o Número")
print("=="*10)

computador = randint(0,10)

escol_jogador = None
cont = 0

while escol_jogador != computador:
    escol_jogador = int(input("Informe um valor entre 0 e 10): "))
    print("Ops!! Tente Novamente!!")
    cont += 1

else:
    print("Você acertou, o computador pensou em {} porém você precisou de {} tentativas kkk".format(computador,cont))
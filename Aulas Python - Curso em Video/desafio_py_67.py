
# ====DESAFIO PYTHON 67 CV ====

# Par ou impar com o computador

from random import randint
from time import sleep

print("--"*20)
print("JOGANDO PAR OU IMPAR COM O PC")
print("--"*20)

vitorias = 0

while True:

    num = int(input("Informe um valor: "))
    tipo = input("PAR OU IMPAR (P/I): ").upper().strip()[0]

    aleatorio = randint(0, 10)

    print("Aguarde o resultado...")
    sleep(5)

    resultado = (num + aleatorio)

    print(f"Você jogou {num} e o computador escolheu {aleatorio}. A soma deu {resultado}.")

    if resultado % 2 == 0:
        valor = "P"
        print(f"O Resultado deu PAR")
    else:
        valor = "I"
        print(f"O Resultado deu IMPAR")

    if tipo == valor:
        print("VOCÊ VENCEU!!")
        vitorias += 1
        continue
    else:
        print("VOCÊ PERDEU")
        print(f"FIM DE JOGO!! Você venceu {vitorias}")
        break






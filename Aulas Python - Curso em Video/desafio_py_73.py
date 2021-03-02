
# ====DESAFIO PYTHON 73 CV ====

# Numeros aletórios e joga na Tupla depois maior e menor valor que estão na tupla
from random import randint

# Dica primeiro transforma os itens em uma lista e depois jogar em uma tupla
# pois as tuplas são imutáveis

lista_aleat = []
for aleat in range(5):
    aleatorio = randint(1,10)
    lista_aleat.append(aleatorio)

    tupla_aleat = tuple(lista_aleat)

print("="*10 + "Tupla Aleatório" + "="*10)
print(f"Valores aleatórios gerados na tupla {tupla_aleat}")

print(f"O maior valor aleatório é {max(tupla_aleat)}")
print(f"O meno valor aleatório é {min(tupla_aleat)}")

# Código do Guanabara
# n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10),)

#Atividade 1

with open('learning_python.txt') as file:
    dados = file.readlines()

    lista = []

    print(dados)

    print("="*80)

    for dado in dados:
        print(dado.strip())
        lista.append(dado.strip())

print("="*80)

print(lista)


print("="*80)
#ATIVIDADE 2

with open('learning_python.txt') as arq:
    arquivo = arq.readlines()

    for arqui in arquivo:
        frases = arqui.replace('Python', 'PHP').strip()
        print(frases)


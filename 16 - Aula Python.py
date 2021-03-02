#Aula 1
#Atividade 1

#carro = input("Qual carro quer Alugar? ")

#print("Irei procurar o {} para você!".format(carro.capitalize()))

#Atividade 2
'''jantar = int(input("Quantas pessoas irão jantar com você? "))

if(jantar > 8):
    print("Espere uma mesa liberar para poder jantar.")
else:
    print("Mesa pronta,")'''

#Atividade 3
'''num = int(input("Informe um número? "))

if(num % 10 == 0):
    print("Multiplo.")
else:
    print("Not Multiplo.")'''

#Teste Aleatório
'''num = 0

while num <= 10:
    num += 1
    if num % 2 == 0:
       continue
    print(num)'''

#Enquete Exemplo Python

ativo = True
questionario = {}
conta = 0

while ativo:
    nome = input("Informe seu Nome: ")
    resposta = input("Qual sua resposta? ")

    questionario[nome] = resposta
    conta += 1

    repetir = input("Obrigado por sua resposta.\n"
          "Deseja responder o questionário? ").lower()

    if repetir == 'não':
        ativo = False


print("Resultados: {} pessoas responderam a enquente.".format(conta))

#Mostrar nomes e respostas
for quest in questionario.items():
    print(quest)
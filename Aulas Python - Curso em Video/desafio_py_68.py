
# ====DESAFIO PYTHON 68 CV ====

maior18 = sexoM = sexIdade = 0

print("---"*30)
print("Desafio Python 68 CV")
print("---"*30)

while True:

    idade = int(input("Informe sua Idade: "))
    sexo = input("Informe seu Sexo [M/F]: ").upper()
    while sexo not in "FM":
        sexo = input("Informe seu Sexo [M/F]: ").upper().strip()[0]

    opcao = input("Deseja cadastrar mais informações [S/N]: ").upper().strip()[0]
    while opcao not in "SN":
        opcao = input("Deseja cadastrar mais informações [S/N]: ").upper().strip()[0]

    if idade > 18:
        maior18 += 1

    # 2
    if sexo == "m":
        sexoM += 1

    # 3
    if sexo == "f" and idade < 20:
        sexIdade += 1

    if opcao == "N":

        #MAIOR DE 18 ANOS QUANTIDADE DE PESSOAS
        print(f"Há {maior18} pessoas maiores de 18 anos.")

        #QUANTOS HOMENS FORAM CADASTRADOS
        print(f"Foram cadastrados {sexoM} homens.")

        #QUANTAS MULHERES TEM MENOS DE 20 ANOS
        print(f"Tem no total de {sexIdade} mulheres com menos de 20 anos.")

        break



# ====DESAFIO PYTHON 69 CV ====

#ESTOQUE BÁSICO

print("---"*30)
print("SISTEMA BASE CAIXA ELETRÔNICO")
print("---"*30)

valor_sacado = int(input("Informe o valor a ser sacado: R$ "))

cedulas50 = (valor_sacado // 50) # OBTEM SAQUE DE CEDULAS DE 50 REAIS
cedulas20 = ((valor_sacado - (50 * cedulas50)) // 20) # OBTEM CEDULAS DE 20 REAIS
cedulas10 = ((valor_sacado - (50 * cedulas50) - (20 * cedulas20)) // 10) # OBTEM CEDULAS DE 10 REAIS
cedulas1 = ((((valor_sacado - (50 * cedulas50)) - (20 * cedulas20)) - (10 * cedulas10)) // 1) # OBTEM CEDULAS DE 1 REAL


print(f"Foram sacadas {cedulas50} cedulas de R$ 50,00") if cedulas50 != 0 else print(end="")
print(f"Foram sacadas {cedulas20} cedulas de R$ 20,00") if cedulas20 != 0 else print(end="")
print(f"Foram sacadas {cedulas10} cedulas de R$ 10,00") if cedulas10 != 0 else print(end="")
print(f"Foram sacadas {cedulas1} cedulas de R$ 1,00") if cedulas1 != 0 else print(end="")


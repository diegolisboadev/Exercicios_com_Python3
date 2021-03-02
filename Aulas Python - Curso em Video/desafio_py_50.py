
#====DESAFIO PYTHON 50 CV ====

#Ler o primeiro termo e razão e mostra os 10 primeiros valores da PA

print('='*25)
print('   10 TERMOS DE UMA PA ')
print('='*25)

primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))

for t in range(primeiro_termo, (primeiro_termo + (9 * razao) + razao), razao):
    print(t, end=' -> ')

print('FIM')
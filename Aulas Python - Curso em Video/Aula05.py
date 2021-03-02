#Aula 09

#Manipulando Strings

frase = 'Curso em Video Python'

print(frase[0:4])#Slice Notation trilhas em Python
print(frase[9])
print(frase[9:13])
print(frase[9:21])#Não é a melhor forma de fatiar até o final
print(frase[9:21:2])#Imprimindo a frase do indice 9 até o indice 21 pulando de 2 em 2
print(frase[:5])#Começa em 0 e vai até o 5 no caso imprimir Curso
print(frase[15:])#Começa do 15 até o final da string
print(frase[9::3])#Começa no indice 9 até o final e pula de 3 em 3
print(len(frase))#Tamanho da string
print(frase.count('o'))#Conta quantas vezes a letra o aparece na string
print(frase.count('o', 0, 13))#Conta quantas vezes a letra 'o' aparece na string do ind 0 ao 13
print(frase.find('deo'))#Mostra em qual indice foi encontrado o 'deo'
print(frase.find('Android'))#Retorna -1 significa que a palavra 'Android' não foi encontrada no string
print('Curso' in frase)#Verificar se a palavra foi encontrada na string se sim retorna True se não False

#Obs. Uma cadeia de caracteres é imutável, ou seja, não dá para modificá-la diretamente, somente usando
#metodos

print(frase.replace('Python', 'Android'))#Alterando um palavra da string por outra temporariamente
print(frase)#Frase original
print(frase.upper())#Tudo na string em maiusculo. obs. o que estiver em maiusculo continuar maiusc
print(frase.lower())#Tudo na string em minusculo. obs. o que estiver em minusculo continuar minsc
print(frase.capitalize())#Somente a primeira letra da string em maiusculo
print(frase.title())#Cada palavra da string com letra inicial maiuscula

frase = '  Aprenda Python  '
print(frase.strip())#Remove todos os espaços da string, tanto da direita como da esquerda
print(frase.rstrip())#Remove todos os espaços da string da direita
print(frase.lstrip())#Remove todos os espaços da string da esquerda

frase = 'Curso em Video Python'
print(frase.split())#Transforma uma string em uma lista mais detalhadamente (dividindo a string pelos
#seus espaços
print('-'.join(frase))#Adiciona um separador entre as palavras da string (junta)

print("""Eric Matthes é professor de ciências e de matemática no Ensino Médio, 
mora no Alasca, onde ministra um curso introdutório de Python. Escreve programas 
desde que tinha cinco anos de idade. Atualmente, Eric tem como foco escrever 
softwares que visam à falta de eficiência na educação e trazer os benefícios 
do software de código aberto a essa área. Em seu tempo livre, gosta de escalar 
montanhas e ficar com sua família.""")#Colocar três aspas duplas para imprimir uma string para imprimir
#um texto muito grande

print(frase.upper().count('O'))#1 transformando a frase em maiusculas e depois verificando
#se tem O maiusculo
frase = frase.replace('Curso', 'Android') #Mudar a palavra da string permanentemente
print(frase)

dividido = frase.split()
print(dividido[2][3]) #Pegar a posição 2 da lista e mostra o conteudo do indice 3




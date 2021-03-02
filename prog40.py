
#ATIVIDADE 40

'''try:
    num1 = int(input("Informe um número: "))
    num2 = int(input("Informe o segundo número: "))

    print("Soma = {}".format(num1 + num2))

except:
    print("Ops! Informe um número não caracteres")'''


#ATIVIDADE 2

'''while True:
    try:
        num1 = int(input("Informe um número: "))
        num2 = int(input("Informe o segundo número: "))
        print("Soma: {}".format(num1 + num2))
    except:
        print("Ops! Informe um número não caracteres")'''

#ATIVIDADE 3 e 4

'''filenames = ['text_files/cats.txt', 'text_files/dog.txt']

for f in filenames:

    try:

        with open(f) as file:
            contents = file.read()
            print(contents)

    except FileNotFoundError:
        #print("Arquivo {} não encontrado.".format(f))
        pass'''

#Atividade 5

line = "Row, row out for row"

print(line.count('row'))
print(line.lower().count('row'))

arquivo = 'text_files/11.txt'

try:
    with open(arquivo) as file:
        contents = file.read()

        palavra = 'in'

        #CONTANDO STRING REPETIDAS
        #ocorrencias = contents.count('read')
        ocorrencias = contents.lower().count(palavra)
        print("Foram encontradas {} ocorrências da palavra {} no text.".format(ocorrencias, palavra.upper()))

except FileNotFoundError:
    pass
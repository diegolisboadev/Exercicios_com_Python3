
#EXCEÇÕES TRY E EXCEPT

try:
    print(5/0)
except ZeroDivisionError:
    print("Erro")


print("novo")


print("Me der 2 numeros vou tentar dividi-los")
print("Digite 'q' para terminar")

'''resposta = ""

while True:
    num1 = input("Informe um número: ").strip()
    if num1 == 'q': break
    num2 = input("Informe outro número: ").strip()
    if num2 == 'q': break

    try:
        resposta = (int(num1) / int(num2))
    except ZeroDivisionError:
        print("Você não pode dividir {} por zero!!".format(str(num1)))


print("Resultado: " + str(resposta))'''

filename = 'alice.txt'

try:
    with open(filename) as file:
        arq = file.read()
        #print(arq)
except FileNotFoundError:
    msg = "Desculpe o arquivo {} não existe!".format(filename.upper())

print(msg)


#TESTE 3

title = "Alice In Wonderland"

print(title.split())


def count_words(filename):
    """conta aproximadamente a quantidade de palavras em um livro"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        #msg = "O arquivo {} não existe!".format(filename)
        #print(msg)
        pass

    else:
        # conta o número aproximado de palavras no arqui
        words = contents.split()
        num_words = len(words)
        print("O arquivo {} tem {} palavras.".format(filename.title(), num_words))


filename = "text_files/11.txt"

count_words(filename)

print("="*50)

filenames = ['text_files/11.txt', 'text_files/guest.txt', 'text_files/learning_python.txt']

for f in filenames:
    count_words(f)

#CREATE, OPEN, READ ARCHIVES PYTHON

#Abrir arquivo
'''with open('text_files/pi.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())'''

'''with open('text_files/pi.txt') as file_object:
    for line in file_object:
        print(line.rstrip())'''

'''with open('text_files/pi.txt') as file_object:
    lines = file_object.readlines()
    pi_string = ''

    for line in lines:
        pi_string += line.strip() #line.rstrip()

print(pi_string[:10] + "...")
print(len(pi_string))'''

'''with open('text_files/pi.txt') as file_object:
    lines = file_object.readlines()

    pi_string = ''

    niver = input("Informe sua data de aniversário (mmddyy): ").strip()

    for line in lines:
        pi_string += line.strip()

if niver in pi_string:
    print("Data contida!")
else:
    print("Data não contida!")'''

print("=="*80)

with open('text_files/pi.txt', 'r+') as file:
    file.write("\nOlá me chamo Diego!\n")
    arqui = file.readlines()

    for f in arqui:
        print(f)







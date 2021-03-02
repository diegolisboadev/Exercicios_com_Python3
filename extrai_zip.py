# coding: utf-8

import os
import zipfile as zip
import sys


# PATH = 'C:\Users\Diego Lisboa\Downloads\dados.zip'


def descompactar():
    path = input('Insira o arquivo a ser descompactado (ex. exemplo.zip) ')

    if not os.path.exists(path):
        print('Arquivo {} não existe'.format(path))
        sys.exit(-1)
    else:
        zfile = zip.ZipFile(path)
        zfile.extractall()
        print('Arquivos extraídos')


def main():
    print('Dica: Coloque este Script dentro do diretório do arquivo a ser '
          'descompactado e execute-o')

    descompactar()


# Função main() com parametro passando o path do arquivo
# def main(PATH):

# if not os.path.exists(PATH):
# print('Arquivo {} não existe'.format(PATH))
# sys.exit(-1)
# else:
# zfile = zip.ZipFile(PATH)
# zfile.extractall()
# print('Arquivos extraídos')


if __name__ == "__main__":
    # main(sys.argv[1])#Quando a função main() recebe parametro
    main()

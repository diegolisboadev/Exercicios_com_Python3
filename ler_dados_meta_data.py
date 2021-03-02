#Ler os arquivos de meta-dados

def read_meta_data(path):
    data = open(path, 'rt')
    meta_data = []
    for line in data:
        line_data = line.slipt('\t')
        meta_data.append((line_data[0],
                         line_data[1],
                         line_data[2]))

    data.close()
    return meta_data

#def main():
#    path = input('Caminho do Arquivo ')
#    read_meta_data(path)

#if __name__ == '__main__':
#    main()
    
read_meta_data('data/meta-data/Instituicao.txt')

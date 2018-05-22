

def main():
    topo = {}
    file = open('berlin52.txt', 'r')
    for i in range(4):
        conteudo = file.readline().strip('\n').split(": ")
        topo[conteudo[0]] = conteudo[1]
    dimenssao = topo['DIMENSION']
    print (dimenssao)


main()

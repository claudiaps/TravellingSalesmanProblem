import math
import genetico

def euclidiana(x1, x2, y1, y2):
    x = (x1 - x2)*(x1 - x2)
    y = (y1 - y2)*(y1 - y2)
    return math.sqrt(x + y) 


def main():

    topo = {}
    file = open('berlin52.txt', 'r') #leitura do arquivo
    for i in range(5):
        conteudo = file.readline().strip('\n').split(": ") 
        topo[conteudo[0]] = conteudo[1]
    dimenssao = int(topo['DIMENSION'])

    file.readline() #pula linha
    vet = [0 for i in range(dimenssao+1)]
    for i in range(1, dimenssao+1): #passa as linhas do arquivo para um vetor, pulando o numero da linha
        vet[i] = file.readline().strip('\n').split(' ')[1:]
        vet[i][0] = float(vet[i][0])
        vet[i][1] = float(vet[i][1])

    matriz = [[0 for i in range(dimenssao+1)] for i in range(dimenssao+1)] #matriz de adjacência
    
    #preenche a matriz com a distancia euclidiana dos pontos do vetor 
    for i in range(1, dimenssao+1): 
        for j in range(1, dimenssao+1):
            matriz[i][j] = euclidiana(vet[i][0], vet[j][0], vet[i][1], vet[j][1])

    # print(matriz)
    genetico.gerar_populacao(52)

main()

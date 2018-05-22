import random

def populacao_aleatoria(n):
    vet = range(1, n+1)
    individuo = random.sample(vet, n)
    return individuo

def gerar_populacao(n):
    populacao = []
    for i in range(n):
        populacao.append(populacao_aleatoria(n)) 
    print(populacao)

def fitness(individuo, matriz):
    soma = 0
    for i in range(len(individuo)-1):
        soma = soma + matriz[individuo[i]][individuo[i+1]]
    soma = soma + matriz[individuo[0]][individuo[-1]]

def crossover_ordenado(individuo):
    p = []
    filho = individuo
    qtd = random.randint(1, len(individuo))
    p = random.sample(range(len(individuo), qtd)
    p.sort()


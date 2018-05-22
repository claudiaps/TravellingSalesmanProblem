import random


def populacao_aleatoria(n):
    vet = range(1, n+1)
    individuo = random.sample(vet, n)
    return individuo


def gerar_populacao(n):
    populacao = []
    for i in range(n):
        populacao.append(populacao_aleatoria(n))
    return populacao


def acumular(populacao):
    res = []
    acum = 0
    for i in populacao:
        res.append(i + acum)
        acum = res[-1]
    return res


def random_select(populacao, n, matriz):
    fit = []
    for i in range(n):
        fit.append(fitness(populacao[i], matriz))
    soma = sum(fit)
    norm = map(lambda x: x/soma, fit)
    acm = acumular(norm)
    r = random.random()
    for i in range(len(acm)):
        if r < acm[i]:
            return populacao[i]


def fitness(individuo, matriz):
    soma = 0
    for i in range(len(individuo)-1):
        soma = soma + matriz[individuo[i]][individuo[i+1]]
    soma = soma + matriz[individuo[0]][individuo[-1]]
    return individuo


def crossover_ordenado(individuo, individuo2):
    p = []
    r = individuo
    qtd = random.randint(1, len(individuo)-1)
    p = random.sample(range(len(individuo)), qtd)
    p.sort()
    s = [0 for i in range(len(p))]
    for i in range(len(p)):
        s[i] = individuo[p[i]]
    p_ord = []
    for i in range(len(individuo2)):
        if individuo2[i] in s:
            p_ord.append(s.index(individuo2[i]))
    for i in range(len(s)):
        r[p[i]] = s[p_ord[i]]

    return r


def crossover_alternativo(p1, p2):
    corte = random.randint(0, len(p1)-1)
    r = p1
    for i in range(corte, len(p1)):
        if r[i] not in p2[:corte] and p2[i] not in r[:corte]:
            r[r.index(p2[i])] = r[i]
            r[i] = p2[i]

    return r


def mutacao1(individuo):
    a = random.randint(0, len(individuo)-1)
    b = random.randint(0, len(individuo)-1)
    aux = individuo[a]
    individuo[a] = individuo[b]
    individuo[b] = aux
    return individuo


def mutacao2(individuo):
    k = random.randint(0, len(individuo)-1)
    print(k)
    for i in range(0, len(individuo)-k, k):
        aux = individuo[i]
        individuo[i] = individuo[i+k]
        individuo[i+k] = aux
    return individuo


def genetico(matriz, n):
    populacao = gerar_populacao(n)
    

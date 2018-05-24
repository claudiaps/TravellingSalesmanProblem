import random


def populacao_aleatoria(n):
    vet = range(1, n+1)
    individuo = random.sample(vet, n)
    return individuo


def gerar_populacao(n, dim):
    populacao = []
    for i in range(n):
        populacao.append(populacao_aleatoria(dim))
    return populacao


def acumular(populacao):
    res = []
    acum = 0
    for i in populacao:
        res.append(i + acum)
        acum = res[-1]
    return res


def random_select(populacao, matriz):
    fit = []
    for i in range(len(populacao)):
        fit.append(1/fitness(populacao[i], matriz))
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
    return soma


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
    k = random.randint(1, len(individuo)-1)
    for i in range(0, len(individuo)-k, k):
        aux = individuo[i]
        individuo[i] = individuo[i+k]
        individuo[i+k] = aux
    return individuo


def genetico(mutacao, populacao, f, n_iter, tx_mutacao, matriz, crossover, parada, elitismo=None):
    pop = populacao
    contador = parada
    aux = []
    aux2 = []
    soma = 0
    soma2 = 0
    fit = list(map(lambda x: f(x, matriz), pop))
    melhor_fit = min(fit)
    melhor_caminho = pop[fit.index(melhor_fit)]
    for gen in range(1):
        p_nova = []
        for i in range(len(populacao)):
            x = random_select(pop, matriz)
            y = random_select(pop, matriz)
            if crossover == 'alternativo':
                novo = crossover_alternativo(x, y)
            elif crossover == 'ordenado':
                novo = crossover_ordenado(x, y)
            r = random.randrange(0, 100)
            if r < tx_mutacao:
                if mutacao == 'mutacao1':
                    novo = mutacao1(novo)
                elif mutacao == 'mutacao2':
                    novo = mutacao2(novo)
            p_nova.append(novo)

        for i in range(len(pop)):
            aux.append(fitness(pop[i], matriz))
            aux2.append(fitness(p_nova[i], matriz))
            soma = sum(aux) + soma
            soma2 = sum(aux2) + soma2
        if soma < soma2:          
            contador = contador - 1
            if contador <= 0:
                break
        else:
            contador = parada
        print('pop ', fit)
        fit_novo = list(map(lambda x: f(x, matriz),p_nova))
        print('p_nova ', fit_novo)

        if elitismo == 'elitismo':
            for k in range(len(pop)):
                for j in range(len(pop)):
                    if fitness(pop[k], matriz) > fitness(p_nova[j], matriz) and p_nova[j] not in pop:
                        print('teste', fitness(pop[k], matriz), fitness(p_nova[j], matriz))
                        pop[k] = p_nova[j]
        fit_novo = list(map(lambda x: f(x, matriz),pop))
        print('nova pop ', fit_novo)
        
        # else:
        #     pop = p_nova
        fit = list(map(lambda x: f(x, matriz), pop))
        fit_local = min(fit)
        if melhor_fit > fit_local:
            melhor_fit = fit_local
            melhor_caminho = pop[fit.index(fit_local)]

    return melhor_caminho, melhor_fit

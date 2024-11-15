import random
import matplotlib.pyplot as plt

# не понятное название функции и переменных
def funct(grph, numb_of_iter, numb_ants, alpha, beta, evap):
    N = len(grph)
    best_path = []
    shortest_dist = float("inf")
    pher = [[1 for i in range(N)] for j in range(N)]
    
    for i in range(numb_of_iter):
        ants_paths = []
        ants_dists = []
        for a in range(numb_ants):
            pos = random.randint(0, N - 1)
            pth = [pos]
            d = 0
            for t in range(N - 1):
                p = []
                for nxt in range(N):
                    if nxt not in pth:
                        p.append((pher[pos][nxt]**alpha) * ((1 / grph[pos][nxt])**beta))
                    else:
                        p.append(0)
                sm = sum(p)
                if sm == 0:
                    nxt = random.choice([x for x in range(N) if x not in pth])
                else:
                    probs = [x / sm for x in p]
                    nxt = random.choices(range(N), probs)[0]
                d += grph[pos][nxt]
                pth.append(nxt)
                pos = nxt
            d += grph[pth[-1]][pth[0]]
            pth.append(pth[0])
            ants_paths.append(pth)
            ants_dists.append(d)
        for k in range(len(pher)):
            for j in range(len(pher[k])):
                pher[k][j] *= (1 - evap)
        for a in range(len(ants_paths)):
            for j in range(len(ants_paths[a]) - 1):
                pher[ants_paths[a][j]][ants_paths[a][j+1]] += 1 / ants_dists[a]
        mn = min(ants_dists)
        if mn < shortest_dist:
            shortest_dist = mn
            best_path = ants_paths[ants_dists.index(mn)]
    
    return shortest_dist, best_path

# граф
grph = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

# вызов функции
res, bpth = funct(grph, 100, 10, 1, 2, 0.5)
print("Лучший путь:", bpth)
print("Минимальная длина:", res)

# визуализация
def draw_grph(grph, path):
    coords = [(0, 0), (2, 3), (4, 1), (6, 4)]
    for i in range(len(grph)):
        for j in range(len(grph[i])):
            if i != j:
                plt.plot([coords[i][0], coords[j][0]], [coords[i][1], coords[j][1]], 'gray', linestyle="dotted")
    for i in range(len(path) - 1):
        a, b = path[i], path[i+1]
        plt.plot([coords[a][0], coords[b][0]], [coords[a][1], coords[b][1]], 'red')
    for i, c in enumerate(coords):
        plt.scatter(c[0], c[1], color='blue')
        plt.text(c[0] + 0.2, c[1] + 0.2, str(i))
    plt.show()

draw_grph(grph, bpth)
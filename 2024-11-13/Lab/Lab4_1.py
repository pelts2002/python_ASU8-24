import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def gen_coords(n):
    c = []
    for i in range(n):
        x = random.uniform(-1000000, 1000000)
        y = random.uniform(-1000000, 1000000)
        z = random.uniform(-1000000, 1000000)
        c.append((x, y, z))
    return c

def gen_roads(n):
    roads = set()
    for i in range(n):
        num_connections = random.randint(1, 2)  # 1 или 2 дороги для каждой точки
        connections = random.sample(range(n), num_connections)  # Выбираем случайные точки
        for j in connections:
            if i != j:  # Исключаем связь с самой собой
                road_type = random.choice(['one-way', 'two-way'])
                roads.add((i, j))
                if road_type == 'two-way':
                    roads.add((j, i))
    return list(roads)

n = 500  # Количество точек
coords = gen_coords(n)
roads = gen_roads(n)

# Визуализация
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Рисуем точки
xs = [coord[0] for coord in coords]
ys = [coord[1] for coord in coords]
zs = [coord[2] for coord in coords]

ax.scatter(xs, ys, zs, c='r', marker='o', label='Точки')

# Рисуем дороги (линии между точками)
for road in roads:
    point1 = coords[road[0]]
    point2 = coords[road[1]]
    ax.plot([point1[0], point2[0]], [point1[1], point2[1]], [point1[2], point2[2]], c='b', alpha=0.5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.title(f"Точки: {n}")
plt.show()

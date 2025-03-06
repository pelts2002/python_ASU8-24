import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#загружаем данные
iris = load_iris()
X = iris.data[:, :2]  
y = iris.target

#масштабируем данные для улучшения работы алгоритма
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#создаём модели k-средних
kmeans = KMeans(n_clusters=3, random_state=42)

#обучаем модели
kmeans.fit(X_scaled)

#получаем центры кластеров и предсказания
centr = kmeans.cluster_centers_
labels = kmeans.labels_

#рисуем график
plt.figure(figsize=(8,6))

#рисуем точки с цветом по кластеру
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap='viridis', edgecolors='k', marker='o')

#рисуем центры кластеров
plt.scatter(centr[:, 0], centr[:, 1], c='red', marker='X', s=200, label='Центры')

#строим график
plt.title('K-средних')
plt.xlabel('Признак 1')
plt.ylabel('Признак 2')
plt.colorbar(label='Метка кластера')
plt.legend()
plt.show()
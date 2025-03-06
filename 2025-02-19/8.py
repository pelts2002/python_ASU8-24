import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import SpectralClustering

#загружаем данные
iris = load_iris()
X = iris.data[:, :2]  

#создаём модели спектральной кластеризации
spectral = SpectralClustering(n_clusters=3, affinity='nearest_neighbors', random_state=42)

#обучаем модели и предсказание кластеров
labels = spectral.fit_predict(X)

#рисуем наши результаты
plt.figure(figsize=(8, 6))

#рисуем точки с цветом по кластеру
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', edgecolors='k', marker='o')

#ещё раз рисуем
plt.title('спектральная кластеризация')
plt.xlabel('Признак 1')
plt.ylabel('Признак 2')
plt.colorbar(label='Метка кластера')
plt.show()
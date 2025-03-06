import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import dendrogram, linkage

#загружаем данные
iris = load_iris()
X = iris.data[:, :2]

#иерархическая кластеризация методом Уорда
Z = linkage(X, method='ward')

#строим дендрограмму
plt.figure(figsize=(10, 7))
dendrogram(Z)
plt.title('дендрограмма методом Уорда')
plt.xlabel('образцы')
plt.ylabel('расстояние')
plt.show()
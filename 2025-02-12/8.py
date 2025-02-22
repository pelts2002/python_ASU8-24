import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA

#загружаем данные
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

#нормализуем данные
normalizuem = X - X.mean()

#строим матрицу ковариации
matrica = np.cov(normalizuem, rowvar=False)

#диагонализация
chisla, vectors = np.linalg.eig(matrica)

#сортируем собственные значения
sorted_indices = np.argsort(chisla)[::-1]
sorted_chisla = chisla[sorted_indices]

#находим долю объяснённой дисперсии
explained_variance_ratio = sorted_chisla / np.sum(sorted_chisla)
cumulative_variance = np.cumsum(explained_variance_ratio)

#строим график метода локтя
plt.figure(figsize=(8, 5))
plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker='o', linestyle='-')
plt.xlabel('Число главных компонент')
plt.ylabel('Накопленная объяснённая дисперсия')
plt.title('Метод локтя для выбора числа главных компонент')
plt.grid()
plt.show()
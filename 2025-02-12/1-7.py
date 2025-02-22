import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA

#загружаем данные
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

#нормализируем их
normalizuem = X - X.mean()

#строим матрицу ковариации
matrica = np.cov(normalizuem, rowvar=False)

#делаем диаганализацию
chisla, vectors = np.linalg.eig(matrica)

#сортируем вектора
sorted_indices = np.argsort(chisla)[::-1]
sorted_vectors = vectors[:, sorted_indices]

#сколько главных компонент
K = 5
selected_vectors = sorted_vectors[:, :K]

#модифицируем их
modification = np.dot(normalizuem, selected_vectors)

#создаём DataFrame для снижения размерности
data_frame = pd.DataFrame(modification, columns=[f'PC{i+1}' for i in range(K)])

#выводим результаты
print("Модифицированные данные (размерность):", modification.shape)
print(modification)
print("\nДанные сниженной размерности (размерность):", data_frame.shape)
print(data_frame)



#готовая реализация PCA из sklearn + вывод
pca = PCA(n_components=K)
X_pca = pca.fit_transform(X)
print("\nДанные после применения встроенного PCA (размерность):", X_pca.shape)
print(X_pca)
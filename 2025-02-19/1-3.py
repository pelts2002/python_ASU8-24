import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#загружаем данные
iris = load_iris()
X = iris.data[:, :2]
y = iris.target

#разделяем на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#тренируем классификатор knn
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

#прогнозируем на тестовых данных
y_pred = knn.predict(X_test)

#оцениваем точность модели
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

#рисуем картинку
h = .02  #шаг в сетке
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

#рисуем контур и точки данных
plt.contourf(xx, yy, Z, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', marker='o', s=100, cmap=plt.cm.Paired)
plt.title('классификация')
plt.xlabel('Признак 1')
plt.ylabel('Признак 2')
plt.show()

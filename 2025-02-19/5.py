import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC  # Импортируем классификатор SVM
from sklearn.metrics import accuracy_score, classification_report

#загружаем данные
iris = load_iris()
X = iris.data[:, :2]
y = iris.target

#разделяем на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#создаём модели SVM
clf = SVC(kernel='linear', random_state=42)  #юзаем линейное ядро для SVM

#обучаем модели
clf.fit(X_train, y_train)

#прогнозируем на тестовых данных
y_pred = clf.predict(X_test)

#рисуем график
plt.figure(figsize=(8,6))

#создаём сетку для визуализации границ решения
h = .02  #размер шага для сетки
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

#рисуем границу решений
plt.contourf(xx, yy, Z, alpha=0.3, cmap='viridis')

#рисуем данные
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='viridis', edgecolors='k', marker='o')
plt.title('SVM')
plt.xlabel('Признак 1')
plt.ylabel('Признак 1')
plt.colorbar(label='Predicted class')
plt.show()
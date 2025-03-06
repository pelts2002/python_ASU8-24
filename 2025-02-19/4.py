import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier  # Добавил импорт
from sklearn.metrics import accuracy_score, classification_report

#загружаем данные
iris = load_iris()
X = iris.data[:, :2]
y = iris.target

#разделяем на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#создаём модели случайного леса
clf = RandomForestClassifier(n_estimators=100, random_state=42)

#обучаем модели
clf.fit(X_train, y_train)

#прогнозируем на тестовых данных
y_pred = clf.predict(X_test)

# Визуализация результатов
plt.figure(figsize=(8,6))
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='viridis')
plt.title('Random Forest Classifier - Prediction')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar(label='Predicted class')
plt.show()
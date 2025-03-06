"""
1. Used pairplot

2. В наборе данных нет столбца 'class', но целевой столбец — это последний
столбец с метками (0 или 1). В коде используется df.columns[-1], чтобы работать с этим столбцом.

3. Точность 98% — это хороший результат, но важно учитывать, что для некоторых
задач важно знать, сколько ошибок модель делает, помимо точности. Для базовой классификации это отличное значение.
"""

#################
# СЛУЧАЙНЫЙ ЛЕС #
#################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#подключаем локальный файл, только первые 500 строк, ибо ПК к черту взлетает
df = pd.read_csv('HTRU_2.csv', header=None, nrows=500)

#делим данные на признаки и целевую переменную
X = df.drop(df.columns[-1], axis=1)  #все столбцы, кроме последнего
y = df[df.columns[-1]]

#делим на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#применяем алгоритм случайного леса
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

#рисуем с помощью pairplot
sns.pairplot(df, hue=df.columns[-1], palette='viridis')
plt.show()
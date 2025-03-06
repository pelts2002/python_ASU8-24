###############
# МЕТОД УОРДА #
###############

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

#подключаем файл
file_path = 'dataset.txt'
data = pd.read_csv(file_path, delimiter="|", header=None, usecols=[2], nrows=500)  #берем первые 500 значений, ибо комп летит к чертям

#преобразуем текст в число
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(data[2])

#кластеризируем методом уорда
Z = linkage(X.toarray(), method='ward')

#рисуем дендограмму
plt.figure(figsize=(10, 7))
dendrogram(Z)
plt.title('дендограмма')
plt.xlabel('индекс')
plt.ylabel('евклидово расстояние')
plt.show()
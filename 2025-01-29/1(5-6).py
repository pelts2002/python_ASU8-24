import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data.csv')

df['Ощущаемая температура (C)'] = df['Apparent Temperature (C)'].astype(float)
df['Влажность'] = df['Humidity'].astype(float)
df['Скорость ветра (км/ч)'] = df['Wind Speed (km/h)'].astype(float)

df['Целевая переменная'] = df['Влажность'] + df['Скорость ветра (км/ч)']  #сумма влажности и скорости ветра

X = df[['Ощущаемая температура (C)']]  #признак: ощущаемая температура
y = df['Целевая переменная']  #целевая переменная: сумма влажности и скорости ветра

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)	#разделяем данные на обучающую и тестовую выборки

model = LinearRegression()	#обучаем модель
model.fit(X_train, y_train)

y_pred = model.predict(X_test)	#предсказываем на тестовых данных

plt.figure(figsize=(10, 6))	#делаем красиво 

sns.scatterplot(x=X_test['Ощущаемая температура (C)'], y=y_test, label='Истинные значения', color='blue')	#диаграмма расеяния для реальных значений

sorted_indices = X_test['Ощущаемая температура (C)'].argsort()  #линия регрессии
plt.plot(X_test['Ощущаемая температура (C)'].iloc[sorted_indices], y_pred[sorted_indices], color='red', label='Линия регрессии')

plt.title('Ощущаемая температура vs Сумма Влажности и Скорости ветра')
plt.xlabel('Ощущаемая температура (C)')
plt.ylabel('Сумма Влажности и Скорости ветра')
plt.legend()
plt.show()
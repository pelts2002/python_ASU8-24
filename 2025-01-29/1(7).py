import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('data.csv')

df['Ощущаемая температура (C)'] = df['Apparent Temperature (C)'].astype(float)
df['Влажность'] = df['Humidity'].astype(float)
df['Скорость ветра (км/ч)'] = df['Wind Speed (km/h)'].astype(float)
df['Целевая переменная'] = df['Влажность'] + df['Скорость ветра (км/ч)']

#признаки + целевую переменную
X = df[['Влажность', 'Целевая переменная']] 
y = df['Ощущаемая температура (C)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)	#разделяем данные на обучающую и тестовую выборки

model = LinearRegression()	#обучаем модель линейной регрессии
model.fit(X_train, y_train)

X_last_30_days = df.tail(30)[['Влажность', 'Целевая переменная']]  #прогнозик на 30 дней

predicted_temperatures = model.predict(X_last_30_days)	#получаем магию

for i, temp in enumerate(predicted_temperatures, 1):	#выводим результаты для 30 дней
    print(f"Предсказанная ощущаемая температура на день {i}: {temp:.2f}°C")

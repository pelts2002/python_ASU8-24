import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dannie = pd.read_csv('data.csv')	#загружаем данные

dannie['Humidity'] = dannie['Humidity'].astype(float)	#првоеряем их
dannie['Apparent Temperature (C)'] = dannie['Apparent Temperature (C)'].astype(float)

X = dannie[['Humidity']]  #влажность
y = dannie['Apparent Temperature (C)']  #температура

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)	#разделяем на обучающую и тестовую выборки

model = LinearRegression()	#обучаем модель линейной регрессии
model.fit(X_train, y_train)

y_pred = model.predict(X_test)	#предсказание

plt.figure(figsize=(10, 6))	#рисуем красоту и линию красненькую
sns.scatterplot(x=X_test['Humidity'], y=y_test, label='True values')
sns.lineplot(x=X_test['Humidity'], y=y_pred, color='red', label='Regression line')

plt.title('Регрессия')
plt.xlabel('Влажность')
plt.ylabel('Ощущаемая температура')
plt.legend()
plt.show()
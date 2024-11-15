import json
import random
from collections import Counter

with open("countries-data.json", "r", encoding="utf-8") as file: countries_data = json.load(file)

#задание 1.1: сортируем страны по названию
sorted_by_name = sorted(countries_data, key=lambda country: country['name'])
print("Страны, отсортированные по названию:")
print([country['name'] for country in sorted_by_name])

#задание 1.2: сортируем страны по столице
sorted_by_capital = sorted(countries_data, key=lambda country: country['capital'] if 'capital' in country and country['capital'] else 'No Capital')
print("\nСтраны, отсортированные по столице:")
print([country['capital'] if 'capital' in country else 'No Capital' for country in sorted_by_capital])

#задание 1.3: сортируем страны по численности населения
sorted_by_population = sorted(countries_data, key=lambda country: country['population'])
print("\nСтраны, отсортированные по численности населения:")
print([(country['name'], country['population']) for country in sorted_by_population])
print("-------------------------------------------------------------------------------------------------------------------------------")

#задание 2
languages_counter = Counter()
for country in countries_data:  #считаем кол-во стран, использующих язык
    if 'languages' in country:
        for language in country['languages']:
            languages_counter[language] += 1

#выбираем наиболее распространенные языки
random_number = random.randint(10, 15)
most_common_languages = languages_counter.most_common(random_number)
print(random_number, " наиболее распространенных языков и количество стран, где их используют:")
for language, count in most_common_languages:
    print(f"{language}: {count} стран")
print("-------------------------------------------------------------------------------------------------------------------------------")

#задание 3. Сортируем страны по населению в убывающем порядке
sorted_by_population = sorted(countries_data, key=lambda country: country['population'], reverse=True)

random_number2 = random.randint(10, 15)
top_population = sorted_by_population[:random_number2]

print(random_number2, " наиболее населенных стран:")
for country in top_population:
    print(f"{country['name']}: {country['population']}")

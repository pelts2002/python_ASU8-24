import json
from functools import reduce

#задание 1: загружаем список стран из файла countries.json
with open("countries.json", "r", encoding="utf-8") as file: countries = json.load(file)

#задание 2: делаем все страны прописными буквами
big_countries = list(map(str.upper, countries)) 
print("Список стран в верхнем регистре:", big_countries)
print("-------------------------------------------------------------------------------------------------------------------------------")

#задание 3: выводим страны содержащие 'land'
countries_with_land = list(filter(lambda country: 'land' in country.lower(), big_countries))
print("Страны, содержащие 'land':", countries_with_land)
print("-------------------------------------------------------------------------------------------------------------------------------")

#задание 4: выводим страны из 6 символов
countries_with_six_simvols = list(filter(lambda country: len(country) == 6, big_countries))
print("Страны с шестью символами:", countries_with_six_simvols)
print("-------------------------------------------------------------------------------------------------------------------------------")

#задание 5: выводим страны из 6 и более символов
countries_with_six_and_bolee_simvols = list(filter(lambda country: len(country) >= 6, big_countries))
print("Страны с шестью и более символами:", countries_with_six_and_bolee_simvols)
print("-------------------------------------------------------------------------------------------------------------------------------")

#задание 6: выводим страны начинающиеся с буквы 'E'
countries_starting_with_e = list(filter(lambda country: country.startswith('E'), big_countries))
print("Страны, начинающиеся с буквы 'E':", countries_starting_with_e)
print("-------------------------------------------------------------------------------------------------------------------------------")

#задание 7: объединяем все страны в предложение
predlojenie = reduce(
    lambda acc, country: f"{acc}, {country}" if acc else country,
    ["Финляндия", "Швеция", "Дания", "Норвегия", "Исландия"]
)
predlojenie += " являются странами Северной Европы."
print("Предложение:", predlojenie)
print("-------------------------------------------------------------------------------------------------------------------------------")

#задание 8: объединяем map() и filter(). Нижний регистр и кол-во символов у страны=4
zadanie8 = list(
    filter(
        lambda country: len(country) == 4,
        map(str.lower, countries)
    )
)
print("Страны из 4 символов в нижнем регистре:", zadanie8)
print("-------------------------------------------------------------------------------------------------------------------------------")

#задание 9.1: каррирование. Возвращает список содержащий 'land'
def categorize_countries_curry(pattern):
    def inner_countries(countries):
        return list(filter(lambda country: pattern in country.lower(), countries))
    return inner_countries

carrir_countries = categorize_countries_curry('land')(countries) 
print("Страны, содержащие 'land':", carrir_countries)
print("-------------------------------------------------------------------------------------------------------------------------------")

#задание 9.2: замыкание. Возвращает список содержащий 'gua'
def categorize_countries_closure(pattern):
    def filter_countries(countries):
        return list(filter(lambda country: pattern in country.lower(), countries))
    return filter_countries

categorize_by_gua = categorize_countries_closure('gua')
countries_with_gua = categorize_by_gua(countries)
print("Страны, содержащие 'gua':", countries_with_gua)
print("-------------------------------------------------------------------------------------------------------------------------------")

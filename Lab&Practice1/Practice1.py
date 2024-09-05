import random
from itertools import islice

numbers = []
for _ in range(10):
 numbers.append(random.randint(0, 100))
print('--------------------------------------------------------------------------------')
print('1.')
print('Сгенерированный список: ', numbers)
numbers2 = list(reversed(numbers))
print('Перевёрнутый список: ', numbers2)

even_indices = [] 
for i in range(len(numbers)): 
    if i % 2 != 0:
        even_indices.append(numbers[i])
print('--------------------------------------------------------------------------------')
print('2.')
print('Четные по индексу элементы первого списка: ', even_indices)

even_indices2 = list(islice(numbers2, None, None, 2))
print('Нечетные по индексу элементы второго списка: ', even_indices2)

numbers4 = []
for _ in range(20):
 numbers4.append(random.randint(0, 10))
print('--------------------------------------------------------------------------------')
print('3.')
print('Сгенерированный список с повторениями: ', numbers4)
unique_numbers = list(set(numbers4))
print('Список без дубликатов: ', unique_numbers)

print('--------------------------------------------------------------------------------')
print('4.')
strings = [random.choice(['a', 'b', 'c']) for _ in range(10)]
print(strings)
numbers = [random.randint(0, 10) for _ in range(10)]
print(numbers)
data = {s: n for s, n in zip(strings, numbers)}
print(data)
tuples = [(v, [k for k, vv in data.items() if vv == v]) for v in set(data.values())]
print(tuples)

print('--------------------------------------------------------------------------------')
print('5.')

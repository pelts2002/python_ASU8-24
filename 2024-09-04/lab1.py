#venv\Scripts\activate.bat - включение виртуальной среды в cmd

# Зоопарк
zoolist = ['Крокодил Гена', 'Лев Симба', 'Манул Тимофей', 'Утка Скрудж Макдак']

print('В зоопарке находится', len(zoolist), 'животных.')

print('Животные - слева направо:', end=' ')
for item in zoolist:
    print(item, end=', ')

print('\nВчера поселили Дятла Вуди')
zoolist.append('Дятел Вуди')
print('Теперь в зоопарке живут:', zoolist)

print('Произведем сортировку')
zoolist.sort()
print('Отсортированный список животных выглядит так:', zoolist)

print('Первое животное, это', zoolist[0])
olditem = zoolist[0]
del zoolist[0]
print(olditem + ' потерялся')
print('В зоопарке остались:', zoolist)

# Находим индекс элемента 'Манул Тимофей' в списке
index_of_timofey = zoolist.index('Манул Тимофей')

# Выводим элемент перед 'Манул Тимофей'
print('Соседи Манула Тимофея: ' + zoolist[index_of_timofey - 1] + ' и ' + zoolist[index_of_timofey + 1])
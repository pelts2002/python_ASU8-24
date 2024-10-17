class segment_manipulyatora:
    def __init__(self, length, ugol):   #инициализируем segment_manipulyatora: length - Длина сегмента; ugol - Угол поворота
        self.length = length
        self.ugol = ugol

    def __str__(self):  #строковое представление объекта
        return f"Длина сегмента: {self.length} м, Угол поворота: {self.ugol}°"

    def __add__(self, other):   #складываем оба segment_manipulyatora: other - Другой сегмент манипулятора; return - Новый сегмент с суммой углов и длины
        return segment_manipulyatora(self.length + other.length, self.ugol + other.ugol)

    def __sub__(self, other):   #вычитаем оба segment_manipulyatora: other - Другой сегмент манипулятора; return - Новый сегмент с разницей углов и длины
        return segment_manipulyatora(self.length - other.length, self.ugol - other.ugol)

class Manipulator:
    def __init__(self, segments):   #инициализируем манипулятор с несколькими сегментами: segments - Список сегментов манипулятора.
        self.segments = segments  #список сегментов

    def total_length(self): #возращаем общую длину манипулятора
        return sum(segment.length for segment in self.segments)

    def total_ugol(self):  #возращаем общий угол поворота манипулятора
        return sum(segment.ugol for segment in self.segments)

    def __str__(self):  #Строковое представление манипулятора
        segments_info = "\n".join([str(segment) for segment in self.segments])
        return f"Манипулятор с сегментами:\n{segments_info}\nОбщая длина: {self.total_length()} м, Общий угол: {self.total_ugol()}°"

    def __add__(self, other):   #складываем манипуляторы: other - Другой манипулятор; return - Новый манипулятор.
        new_segments = [s1 + s2 for s1, s2 in zip(self.segments, other.segments)]
        return Manipulator(new_segments)

    def __sub__(self, other):   #вычитаем манипуляторы: other - Другой манипулятор; return - Новый манипулятор.
        new_segments = [s1 - s2 for s1, s2 in zip(self.segments, other.segments)]
        return Manipulator(new_segments)


segment1 = segment_manipulyatora(1.5, 30)   #пример!
segment2 = segment_manipulyatora(1.0, 45)
segment3 = segment_manipulyatora(2.0, 15)

segment4 = segment_manipulyatora(1.5, 60)
segment5 = segment_manipulyatora(1.0, 30)
segment6 = segment_manipulyatora(2.0, 10)

manipulator1 = Manipulator([segment1, segment2, segment3])  #создаем два манипулятора с тремя сегментами
manipulator2 = Manipulator([segment4, segment5, segment6])

print("Манипулятор 1:")
print(manipulator1)

print("\nМанипулятор 2:")
print(manipulator2)

new_manipulator = manipulator1 + manipulator2
print("\nНовый манипулятор после сложения:")
print(new_manipulator)

diff_manipulator = manipulator1 - manipulator2
print("\nНовый манипулятор после вычитания:")
print(diff_manipulator)

"""
перегруженные операторы __add__() и __sub__() позволяют
складывать и вычитать сегменты между манипуляторами.
"""
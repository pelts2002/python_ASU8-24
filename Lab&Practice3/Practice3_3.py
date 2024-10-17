class motor:    #базовый класс для всех движков
    def __init__(self, power, speed, KRmoment):   # инициализируем основные хар-ки движка
        self.power = power  #мощность (Вт)
        self.speed = speed  #скорость вращения (об/мин)
        self.KRmoment = KRmoment  #крутящий момент (Нм)

    def __str__(self):  #строковое представление объекта для пользователя
        return f"Мощность: {self.power} Вт, Скорость: {self.speed} об/мин, Крутящий момент: {self.KRmoment} Нм"

    def __repr__(self):     #строковое представление объекта для разработчика
        return f"Motor(power={self.power}, speed={self.speed}, КРТЩмомент={self.KRmoment})"

    def __eq__(self, other):    #перегружаем операторы для сравнения двигателей по скорости
        return self.speed == other.speed

    def __ne__(self, other):
        return self.speed != other.speed

    def __lt__(self, other):
        return self.speed < other.speed

    def __gt__(self, other):
        return self.speed > other.speed

    def __le__(self, other):
        return self.speed <= other.speed

    def __ge__(self, other):
        return self.speed >= other.speed

class sinxron_motor(motor):  #класс для синхронных двигателей
    def __init__(self, power, speed, KRmoment, KPD_motor):
        super().__init__(power, speed, KRmoment)
        self.KPD_motor = KPD_motor  #КПД двигателя (%)

    def __str__(self):
        return f"Синхронный двигатель: {super().__str__()}, КПД: {self.KPD_motor}%"

class asinxron_motor(motor): #класс для асинхронных двигателей
    def __init__(self, power, speed, KRmoment, voltage):
        super().__init__(power, speed, KRmoment)
        self.voltage = voltage  #напряжение питания (В)

    def __str__(self):
        return f"Асинхронный двигатель: {super().__str__()}, Напряжение: {self.voltage} В"

class liney_motor(motor):   #класс для линейных двигателей
    def __init__(self, power, speed, KRmoment, max_power):
        super().__init__(power, speed, KRmoment)
        self.max_power = max_power  #максимальная сила (Н)

    def __str__(self):
        return f"Линейный двигатель: {super().__str__()}, Макс. сила: {self.max_power} Н"

sync_motor = sinxron_motor(5000, 1500, 10, 95) #используем классы и сравнения
async_motor = asinxron_motor(4000, 1200, 8, 380)
linear_motor = liney_motor(3000, 1800, 6, 500)

print(sync_motor)  #выводим синхронный двигатель
print(repr(async_motor))  #представляем асинхронный двигатель для разработчика

print(sync_motor > async_motor)  #сравниваем: True - синхронный двигатель быстрее асинхронного
print(linear_motor < sync_motor)  # False - линейный двигатель быстрее синхронного


"""
    __str__() используется для пользовательского представления объекта и вызывается функцией print() или при преобразовании объекта в строку.
    __repr__() предназначен для разработчиков и должен возвращать строку, которая содержит достаточно информации для воссоздания объекта.
    Методы __eq__(), __ne__(), __lt__(), __gt__(), __le__(), __ge__() используются для сравнения объектов по скорости вращения.
Это позволяет использовать операторы ==, !=, <, >, <=, >= для экземпляров классов.
"""
class Stek:
    def __init__(self):
        self.stek = [] #инициализируем стек

    def is_empty(self):
        return len(self.stek) == 0 #проверяем, пустой ли стек 

    def push(self, item):
        self.stek.append(item) # добавляем элемент в стек
        print(f"Элемент {item} добавлен в стек.")

    def pop(self):
        if not self.is_empty(): #Удаляем элемент из стека
            removed_item = self.stek.pop()
            print(f"Элемент {removed_item} удален из стека.")
            return removed_item
        else:
            print("Стек пуст, нечего удалять.")
            return None

    def peek(self):
        if not self.is_empty(): # смотрим верхний элемент в стеке
            return self.stek[-1]
        else:
            print("Стек пуст.")
            return None

    def size(self):
        return len(self.stek) #возвращаем размер стека

stek = Stek()
stek.push(1)
stek.push(2)
stek.push(3)
print("Верхний элемент:", stek.peek())
stek.pop()
print("Текущий размер стека:", stek.size())
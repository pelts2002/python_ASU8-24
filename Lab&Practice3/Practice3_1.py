class Ochered: 
    def __init__(self):
        self.ochered = [] #инициализируем очередь

    def is_empty(self):
        return len(self.ochered) == 0 #проверяем, пустая ли очередь

    def enqueue(self, item):
        self.ochered.append(item) #добавляем элемент в конец очереди
        print(f"Элемент {item} добавлен в очередь.")

    def dequeue(self):
        if not self.is_empty(): #удаляем элемент из начала очереди
            removed_item = self.ochered.pop(0)
            print(f"Элемент {removed_item} удален из очереди.")
            return removed_item
        else:
            print("Очередь пуста, нечего удалять.")
            return None

    def peek(self):
        if not self.is_empty(): #смотрим 1ый элемент в очереди, без удаления
            return self.ochered[0]
        else:
            print("Очередь пуста.")
            return None

    def size(self):
        return len(self.ochered) #возращаем размер очереди

ochered = Ochered() 
ochered.enqueue(1)
ochered.enqueue(2)
ochered.enqueue(3)
print("Первый элемент:", ochered.peek())
ochered.dequeue()
print("Текущий размер очереди:", ochered.size())
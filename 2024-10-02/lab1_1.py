import json
import os

class zadachi:  #инициализируем задачи. opisanie_zadachi - Описание задачи. category - Категория задачи. status - Статус выполнения
    def __init__(self, opisanie_zadachi, category, status=False):
        self.opisanie_zadachi = opisanie_zadachi
        self.category = category
        self.status = status

    def mark_completed(self):
        self.status = True  #отмечаем задачу как выполненную

    def to_dict(self):  #преобразовываем задачу в словарь для сохранения в JSON
        return {
            'opisanie_zadachi': self.opisanie_zadachi,
            'category': self.category,
            'status': self.status
        }

    @classmethod
    def from_dict(cls, task_dict):  #создаем задачу из словаря (при загрузке из JSON)
        return cls(
            opisanie_zadachi=task_dict['opisanie_zadachi'],
            category=task_dict['category'],
            status=task_dict['status']
        )

class TaskTracker:
    def __init__(self, filename='tasks.json'):  #инициализируем таск-трекер. filename - Имя файла для хранения задач.
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, opisanie_zadachi, category): #добавляем новую задачу
        task = zadachi(opisanie_zadachi, category)
        self.tasks.append(task)
        print(f"Задача '{opisanie_zadachi}' в категории '{category}' добавлена.")

    def mark_task_completed(self, task_number): #отмечаем задачу как выполенную по её номеру
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number].mark_completed()
            print(f"Задача '{self.tasks[task_number].opisanie_zadachi}' отмечена как выполненная.")
        else:
            print("Неверный номер задачи.")

    def list_tasks(self): #выводим список задач
        if not self.tasks:
            print("Нет задач.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                status = "Выполнено" if task.status else "Не выполнено"
                print(f"{i}. [{status}] {task.opisanie_zadachi} (Категория: {task.category})")

    def save_tasks(self):   #сохраняем задачи в JSON-файл
        with open(self.filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)
        print(f"Задачи сохранены в файл {self.filename}.")

    def load_tasks(self):   #загружаем задачи из JSON-файла
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                task_dicts = json.load(f)
                self.tasks = [zadachi.from_dict(td) for td in task_dicts]
            print(f"Задачи загружены из файла {self.filename}.")
        else:
            print("Файл с задачами не найден, создаем новый список.")

def main(): #основа
    tracker = TaskTracker()

    while True:
        print("\n1. Добавить задачу\n2. Отметить задачу выполненной\n3. Показать задачи\n4. Сохранить и выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            opisanie_zadachi = input("Введите описание задачи: ")
            category = input("Введите категорию задачи: ")
            tracker.add_task(opisanie_zadachi, category)
        elif choice == '2':
            tracker.list_tasks()
            task_number = int(input("Введите номер задачи для отметки как выполненной: ")) - 1
            tracker.mark_task_completed(task_number)
        elif choice == '3':
            tracker.list_tasks()
        elif choice == '4':
            tracker.save_tasks()
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
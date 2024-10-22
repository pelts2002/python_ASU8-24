import json
import os

class Transaction:  #инициализируем транзакцию: opisanie_operation - Описание операции. summa - Сумма операции. category - Категория операции.
    def __init__(self, opisanie_operation, summa, category): 
        self.opisanie_operation = opisanie_operation
        self.summa = summa
        self.category = category

    def to_dict(self):  #преобразовывем транзакцию в словарь для сохранения в JSON
        return {
            'opisanie_operation': self.opisanie_operation,
            'summa': self.summa,
            'category': self.category
        }

    @classmethod
    def from_dict(cls, trans_dict): #создаем транзакцию из словаря
        return cls(
            opisanie_operation=trans_dict['opisanie_operation'],
            summa=trans_dict['summa'],
            category=trans_dict['category']
        )

class controL_operation:    #инициализируем трекер бюджета. filename - Имя файла для хранения данных.
    def __init__(self, filename='budget.json'):
        self.transactions = []
        self.filename = filename
        self.load_transactions()

    def add_transaction(self, opisanie_operation, summa, category): #добавляем новую операцию
        transaction = Transaction(opisanie_operation, summa, category)
        self.transactions.append(transaction)
        print(f"Операция '{opisanie_operation}' на сумму {summa} в категории '{category}' добавлена.")

    def list_transactions(self):    #выводим список всех операций
        if not self.transactions:
            print("Нет операций.")
        else:
            for i, transaction in enumerate(self.transactions, start=1):
                trans_type = "Доход" if transaction.summa > 0 else "Расход"
                print(f"{i}. [{trans_type}] {transaction.opisanie_operation} - {transaction.summa} руб. (Категория: {transaction.category})")

    def get_balance(self):  #рассчитываем общий баланс (сумма всех операций)
        return sum(transaction.summa for transaction in self.transactions)

    def save_transactions(self):    #сохраняем все операции в JSON
        with open(self.filename, 'w') as f:
            json.dump([trans.to_dict() for trans in self.transactions], f, indent=4)
        print(f"Данные сохранены в файл {self.filename}.")

    def load_transactions(self):    #загружаем операции из JSON
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                trans_dicts = json.load(f)
                self.transactions = [Transaction.from_dict(td) for td in trans_dicts]
            print(f"Операции загружены из файла {self.filename}.")
        else:
            print("Файл с операциями не найден, создаем новый список.")

def main(): #основа!
    tracker = controL_operation()

    while True:
        print("\n1. Добавить операцию\n2. Показать операции\n3. Показать баланс\n4. Сохранить и выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            opisanie_operation = input("Введите описание операции: ")
            summa = float(input("Введите сумму операции (положительное для дохода, отрицательное для расхода): "))
            category = input("Введите категорию операции: ")
            tracker.add_transaction(opisanie_operation, summa, category)
        elif choice == '2':
            tracker.list_transactions()
        elif choice == '3':
            print(f"Текущий баланс: {tracker.get_balance()} руб.")
        elif choice == '4':
            tracker.save_transactions()
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
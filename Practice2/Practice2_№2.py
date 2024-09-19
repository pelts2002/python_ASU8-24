import random

# список слов
slova = ['город', 'забор', 'масло', 'носок', 'котик', 'трава', 'дверь', 'лодка', 'школа', 'вилка']

def get_word():
    return random.choice(slova)

def check_guess(secret_slovo, guess):
    result = []
    for i, char in enumerate(guess):
        if char == secret_slovo[i]:
            result.append(f"[{char}]")  
        elif char in secret_slovo:
            result.append(f"({char})")  
        else:
            result.append(char) 
    return ''.join(result)

def play():
    secret_slovo = get_word()
    popytka = 6  

    print("Правильная буква и позиция отмечены: []")
    print("Правильная буква, но неправильная позиция отмечена: ()\n")

    for attempt in range(1, popytka + 1):
        guess = input(f"Попытка {attempt}/{popytka}. Введите слово: ").lower()

        if len(guess) != 5:
            print("Слово должно быть длиной 5 букв.")
            continue

        result = check_guess(secret_slovo, guess)
        print(f"Результат: {result}")

        if guess == secret_slovo:
            print("Поздравляю! Вы угадали слово!")
            break
    else:
        print(f"Вы не угадали. Загаданное слово было: {secret_slovo}")

if __name__ == "__main__":
    play()
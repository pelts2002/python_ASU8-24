import random

def generate_number():
    # генерируем четырехзначное уникаьное число
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(str(digit) for digit in digits[:4])

def get_bulls_and_cows(secret, guess):
    cows = 0 
    bulls = 0  
    for i in range(4):
        if guess[i] == secret[i]:
            cows += 1
        elif guess[i] in secret:
            bulls += 1
    return bulls, cows

def play_game():
    secret_number = generate_number()
    attempts = 0

    print("Загадано четырехзначное число с уникальными цифрами.")
    while True:
        guess = input("Введите четырехзначное число: ")
        
        if len(guess) != 4 or not guess.isdigit():
            print("Пожалуйста, введите корректное четырехзначное число.")
            continue

        attempts += 1
        bulls, cows = get_bulls_and_cows(secret_number, guess)
        print(f"Быки: {bulls}, Коровы: {cows}")

        if cows == 4:
            print(f"Ура! Вы угадали число {secret_number} за {attempts} попыток.")
            break

if __name__ == "__main__":
    play_game()
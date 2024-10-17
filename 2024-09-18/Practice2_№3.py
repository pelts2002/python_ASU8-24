import random

def get_user_choice():
    vybor = {'1': 'Камень', '2': 'Ножницы', '3': 'Бумага'}
    print("\nВыберите одно:")
    print("1 - Камень")
    print("2 - Ножницы")
    print("3 - Бумага")
    user_input = input("Введите ваш выбор (1/2/3): ")
    return vybor.get(user_input)

def get_computer_choice():
    vybor = ['Камень', 'Ножницы', 'Бумага']
    return random.choice(vybor)

def determine_winner(user_vybor, computer_vybor):
    if user_vybor == computer_vybor:
        return "Ничья!"
    elif (user_vybor == 'Камень' and computer_vybor == 'Ножницы') or \
         (user_vybor == 'Ножницы' and computer_vybor == 'Бумага') or \
         (user_vybor == 'Бумага' and computer_vybor == 'Камень'):
        return "Вы выиграли!"
    else:
        return "Хумпуктер выиграл!"

def play_game():
    while True:
        user_vybor = get_user_choice()
        if not user_vybor:
            print("Неправильный ввод. Попробуйте снова.")
            continue

        computer_vybor = get_computer_choice()
        print(f"\nВы выбрали: {user_vybor}")
        print(f"Хумпуктер выбрал: {computer_vybor}")

        result = determine_winner(user_vybor, computer_vybor)
        print(result)

        play_again = input("\nХотите сыграть еще раз? (да/нет): ").lower()
        if play_again != 'да':
            print("good game, goodbye")
            break

if __name__ == "__main__":
    play_game()

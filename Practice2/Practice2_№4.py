def function_deliteley(n):
    if n <= 0 or n > 100000:
        raise ValueError("Число должно быть больше 0 и не больше 100000")
    
    deliteli = []
    prostoy_or_net = True
    
    # Проверка всех чисел от 1 до sqrt(n) на делимость
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            deliteli.append(i)
            if i != n // i:
                deliteli.append(n // i)
            if i != 1:
                prostoy_or_net = False
    
    # Число является простым, если его единственные делители - 1 и оно само
    if n == 1:
        prostoy_or_net = False
    
    return sorted(deliteli), prostoy_or_net

# Ввод числа пользователем
try:
    n = int(input("Введите целое число больше 0 и не больше 100000: "))
    deliteli, prostoy_or_net = function_deliteley(n)
    print(f"Делители числа {n}: {deliteli}")
    print(f"Число {n} {'является простым' if prostoy_or_net else 'не является простым'}")
except ValueError as e:
    print(f"Ошибка: {e}")

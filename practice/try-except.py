try:
    # Запрашиваем у пользователя два числа
    numerator = float(input("Введите числитель: "))
    denominator = float(input("Введите знаменатель: "))

    # Выполняем деление
    result = numerator / denominator

    # Выводим результат
    print("Результат деления:", result)
except ZeroDivisionError:
    # Обработка ошибки деления на ноль
    print("Ошибка: на ноль делить нельзя!")
except ValueError:
    # Обработка ошибки ввода, если введено не число
    print("Ошибка: введено не число.")
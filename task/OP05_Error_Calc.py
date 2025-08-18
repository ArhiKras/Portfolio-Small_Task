# Возьми одну из программ, которую мы писали на прошлых уроках, продумай, какие ошибки в программе могут появляться(можно прям специально пробовать ее ломать) и дополни код конструкцией try-except для обработки выявленных исключений.

while True:
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        operation = input("Введите операцию (+, -, *, /): ")

        if operation == "+":
            print(f"Результат: {num1 + num2}")
        elif operation == "-":
            print(f"Результат: {num1 - num2}")
        elif operation == "*":
            print(f"Результат: {num1 * num2}")
        elif operation == "/":
            print(f"Результат: {num1 / num2}")
        else:
            print("Неизвестная операция")
            break

    except ValueError:
        print("Ошибка: введено не число!")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно")

    print("\n")
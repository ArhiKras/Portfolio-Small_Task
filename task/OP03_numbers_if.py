# Пользователь вводит три различных числа. Напишите программу, которая находит и выводит наименьшее из этих трех чисел.

while True:
    number1 = input("Введите первое число ('стоп' - для выхода): ")
    if number1.lower() == "стоп":
        break
    else:
        number1 = int(number1)
    number2 = input("Введите второе число ('стоп' - для выхода): ")
    if number2.lower() == "стоп":
        break
    else:
        number2 = int(number2)
    number3 = input("Введите третье число ('стоп' - для выхода): ")
    if number3.lower() == "стоп":
        break
    else:
        number3 = int(number3)

    if number1 < number2 and number1 < number3:
        print(f"Наименьшее число: {number1}")
    elif number2 < number1 and number2 < number3:
        print(f"Наименьшее число: {number2}")
    elif number3 < number1 and number3 < number2:
        print(f"Наименьшее число: {number3}")
    else:
        print("Числа равны")
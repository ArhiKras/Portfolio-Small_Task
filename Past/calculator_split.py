user_input = input("Введите операцию: ")
num1, operation, num2 = user_input.split()
# split() разделяет строку на части по пробелам и возвращает список ['1', '+', '2'], но далее необходимо преобразование в int или float
num1 = float(num1)
num2 = float(num2)

if operation == "+":
    print(f"Результат: {num1 + num2}")
elif operation == "-":
    print(f"Результат: {num1 - num2}")
elif operation == "*":
    print(f"Результат: {num1 * num2}")
elif operation == "/":
    if num2 != 0:
        print(f"Результат: {num1 / num2}")
    else:
        print("Деление на ноль невозможно")
else:
    print("Неизвестная операция")


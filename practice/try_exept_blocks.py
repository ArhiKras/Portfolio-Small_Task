try:
    print(3 / 0)
except Exception as e:
    # Exception - базовый класс для всех исключений, можно присвоить переменную и выводить информацию о ошибке
    print(f"Ошибка: {e}")

print("\n")

try:
    number = int(input("Введите число: "))
    print(f"Вы ввели число: {number}")
except:
    # можно не указывать тип ошибки, тогда будет ловить все ошибки - свой print
    print("Преобразование в число не сработало")
print("Программа завершена")

print("\n")

try:
    number = int(input("Введите число: "))
    print(f"Вы ввели число: {number}")
except:
    print("Преобразование в число не сработало")
finally:
    # finally выполняется в любом случае, даже если не было исключения
    print("Выполняется в любом случае")

print("\n")

try:
    number = int(input("Введите число: "))
    print(f"Вы ввели число: {number}")
except:
    print("Преобразование в число не сработало")
else:
    print("try - без ошибок")
finally:
    print("Выполняется в любом случае")
print("Программа завершена")

print("\n")

try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    result = number1 / number2
    print(f"Результат деления: {result}")
except (ZeroDivisionError, ValueError) as e:
    # Можно указать несколько типов ошибок через запятую
    print(f"Ошибка: {e}")
# Создать калькулятор — программу, в которой мы вводим 2 числа, и с ними производятся сразу все математические действия, рассмотренные в уроке.

number_1 = float(input("Введите первое число: "))
number_2 = float(input("Введите второе число: "))

result_1 = number_1 + number_2
result_2 = number_1 - number_2
result_3 = number_1 * number_2
print(f"\nРезультат сложения: {result_1}")
print(f"Результат вычитания: {result_2}")
print(f"Результат умножения: {result_3}")

if number_2 != 0:
    result_4 = number_1 / number_2
    result_5 = number_1 // number_2
    result_6 = number_1 % number_2
    print(f"Результат деления: {result_4}")
    print(f"Результат целочисленного деления: {result_5}")
    print(f"Результат деления по модулю: {result_6}")
else:
    print("Деление невозможно: делить на 0 нельзя.")
    
result_7 = number_1 ** number_2
print(f"Результат возведения в степень: {result_7}")


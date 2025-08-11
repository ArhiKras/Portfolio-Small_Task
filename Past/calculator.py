# Калькулятор


while True:
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
    if num2 != 0:
      print(f"Результат: {num1 / num2}")
    else:
      print("Деление на ноль невозможно")
  else:
    print("Неизвестная операция")
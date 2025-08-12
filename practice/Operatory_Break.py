i = 1
while i <= 10:
  print(i)
  i += 1
else:
  print(f"Цикл завершен, i = {i}")
  
print("\n")

# Оператор Break
num = int(input("Введите число: "))
while num != 0:
  if num < 0:
    print("Число отрицательное")
    break
  num = int(input("Введите число: "))
else:
  print("Цикл завершен, введено число 0")

print("\n")

# Бесконечный цикл
num = int(input("Введите число: "))
while True:
  print(num)
  num += 1
  if num > 10:
    break

print("\n")

# Оператор Continue
print("Введите числа для проверки на нечётность. Для завершения введите 0.")
while True:  # Бесконечный цикл, который будет прерван только при определенном условии
    number = int(input("Введите число: "))
    if number == 0:  # Условие для выхода из цикла
        break
    if number % 2 == 0:  # Проверка на четность
        continue  # Пропускаем четные числа
    print("Нечетное число:", number)  # Выводим нечетное число

print("Программа завершена.")

print("\n")

# Оператор Pass
if number == 0:
  pass  # Заглушка, которая ничего не делает
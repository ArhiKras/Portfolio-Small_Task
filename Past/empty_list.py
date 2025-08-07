# Создаем пустой список
numbers = []

# Добавляем в список несколько чисел
numbers.append(10)
numbers.append(20)
numbers.append(30)
numbers.append(40)
numbers.append(50)

# Выводим содержимое списка
print("Список чисел:", numbers)

# Находим максимальное число в списке
max_number = max(numbers)
print ("Максимальное число:", max_number)

# Вычисляем среднее значение элементов списка
average = sum(numbers) / len(numbers)
print("Среднее значение:", average)
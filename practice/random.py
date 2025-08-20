import random # импорт всех функций из модуля random

# from random import randint, choice импорт конкретной функции из модуля random

result1 = random.randint(1, 6)
result2 = random.random()
result3 = random.choice([1, 2, 3, 4, 5, 6])
result4 = random.randrange(1, 20, 3)
my_list = [1, 2, 3, 4, 5, 6]
result5 = random.shuffle(my_list)
result6 = random.uniform(3, 5)

print(f"Результат: {result1}")
print("\n")
print(f"Результат: {result2}")
print("\n")
print(f"Результат: {result3}")
print("\n")
print(f"Результат: {result4}")
print("\n")
print(f"Результат: {my_list}")
print("\n")
print(f"Результат: {result6}")

# Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения start до величины end включительно.

def sum_range(start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum
sum_enter = sum_range(1, 10)
print(sum_enter)
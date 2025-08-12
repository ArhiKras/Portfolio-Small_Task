# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа, после return перечислить все значения через запятую): периметр квадрата, площадь квадрата и диагональ квадрата.

def square(side):
    perimeter = side * 4
    area = side ** 2
    diagonal = side * (2 ** 0.5)
    return perimeter, area, diagonal
square_enter = square(2)
print(square_enter)
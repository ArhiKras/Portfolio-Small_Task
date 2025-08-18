class MyCustomError(Exception):
    # Базовый класс для всех пользовательских исключений
    pass

def check_number(x):
    if x > 100:
        raise MyCustomError("Число больше 100")
        # raise - вызывает(генерирует) исключение
    elif x < 0:
        raise ValueError("Число меньше 0")
    else:
        print("Число в диапазоне от 0 до 100")

try:
    check_number(101)
except MyCustomError as e:
    print(f"Ошибка: {e}")
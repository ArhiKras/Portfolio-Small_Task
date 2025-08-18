# Напиши функцию safe_divide, которая принимает два аргумента: a и b. Функция должна пытаться делить a на b и возвращать результат. Если произойдет ошибка деления на ноль (ZeroDivisionError), функция должна возвращать None вместо возникновения исключения. Продемонстрируй работу функции на нескольких примерах, включая деление на ноль.



def safe_divide(a, b): 
    try:
        return a / b
    except ZeroDivisionError:
        return None

while True:
    a = input("Введите первое число или 'stop' для выхода из программы: ")
    if a.lower() == "stop":
        print("Выход из программы")
        break
    else:
        a = int(a)
    b = input("Введите второе число или 'stop' для выхода из программы: ")
    if b.lower() == "stop":
        print("Выход из программы...")
        break
    else:
        b = int(b)

    result = safe_divide(a, b)
    print(f"Результат деления: {result}")

    print("\n")
    


    
    
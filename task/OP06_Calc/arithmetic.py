# Создайте модуль arithmetic.py, который будет содержать 4 функции: сложение, вычитание, умножение и деление. Импортируйте модуль в другой файл Python и выполните каждую из функций с произвольными аргументами.

def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return "Неизвестная операция"


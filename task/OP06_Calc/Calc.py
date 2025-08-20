import arithmetic

while True:
    
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    operation = input("Введите операцию (+, -, *, /): ")
    
    print(f"Результат вычисления: {arithmetic.calculator(num1, num2, operation)}")

    print("\n")
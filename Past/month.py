# Month


while True:
    month = input("Введите номер месяца (1-12) или 'стоп' для выхода из программы: ")
    if month.lower() == "стоп":
        break
    else:
        month = int(month)

    if month in (1, 3, 5, 7, 8, 10, 12):
        print("В этом месяце 31 день")
    elif month in (4, 6, 9, 11):
        print("В этом месяце 30 дней")
    elif month == 2:
        print("В этом месяце 28 или 29 дней")
    else:
        print("Неверный ввод. Введите число от 1 до 12")
                                     
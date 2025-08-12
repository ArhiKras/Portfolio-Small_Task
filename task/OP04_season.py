# Написать функцию season, принимающую 1 аргумент - номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или есень).

def seasons(month):
    if 1 <= month <= 12:
        if month == 12 or month == 1 or month == 2:
            return "Зима"
        elif month == 3 or month == 4 or month == 5:
            return "Весна"
        elif month == 6 or month == 7 or month == 8:
            return "Лето"
        elif month == 9 or month == 10 or month == 11:
            return "Осень"
    else:
        print("Такого месяца нет")

season_month = seasons(1)
print(season_month)
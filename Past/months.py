# Months


while True:
  months = input("Введите номер месяца (1-12) или 'стоп' для выхода из программы: ")
  if months.lower() == "стоп":
    break
  else:
    months = int(months)

  if months in (1, 3, 5, 7, 8, 10, 12):
    print("В этом месяце 31 день")
  elif months in (4, 6, 9, 11):
    print("В этом месяце 30 дней")
  elif months == 2:
    print("В этом месяце 28 или 29 дней")
  else:
    print("Неверный ввод. Введите число от 1 до 12")
                   
# Запрос пароля

true_password = "uys5s56rx6"
true_email = "art@mail.ru"
password = input("Введите пароль: ")
if password == true_password:
  print("Пароль верный")
  print("Теперь введите почту")
  email = input("Введите почту: ")
  if email == true_email:
    print("Добро пожаловать!")
  else:
    print("Почта неверная")
else:
  print("Пароль неверный")

# Угадай число

import random

true_number = random.randint(1, 200)
while True:
  answer = int(input("Какое число я загадал (число от 1 до 200) - "))
  if answer < true_number:
    print("Загаданное число больше")
  elif answer > true_number:
    print("Загаданное число меньше")
  else:
    print("Ты угадал!")
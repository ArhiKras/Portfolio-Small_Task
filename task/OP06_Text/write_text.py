# Напишите скрипт, который запрашивает у пользователя текст, а затем записывает этот текст в файл user_data.txt.

text = input("Введите текст: ")

with open("user_data.txt", "w", encoding="utf-8") as file:
    file.write(text + "\n")

print("Текст успешно записан в файл.")
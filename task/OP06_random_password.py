# Напишите простую программу, которая генерирует случайный пароль длиной 8 символов. Пароль должен содержать случайно выбранные строчные и заглавные буквы, цифры и специальные символы. Используйте модуль random для выбора символов.

import random

letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_+"
password = ""

for i in range(8):
    password += random.choice(letters)
    
print(password)
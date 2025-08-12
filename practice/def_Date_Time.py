# Функция для вывода текущей даты и времени
# Импорт модуля datetime
from datetime import datetime 

def print_current_time_and_date():
    now = datetime.now() # Получаем текущую дату и время
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S") # Форматируем дату и время
    print("Текущая дата и время:", formatted_now)

print_current_time_and_date()
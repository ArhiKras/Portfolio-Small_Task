from datetime import datetime
import pytz

# Часовые пояса
moscow_tz = pytz.timezone("Europe/Moscow")
novosibirsk_tz = pytz.timezone("Asia/Novosibirsk")

# Ввод направления
print("Конвертер времени между Новосибирском и Москвой")
print("1 — Новосибирск → Москва")
print("2 — Москва → Новосибирск")
direction = input("Выберите направление (1 или 2): ")

# Ввод времени
user_time_str = input("Введите время в формате ГГГГ-ММ-ДД ЧЧ:ММ: ")

try:
    # Преобразуем строку во время
    naive_time = datetime.strptime(user_time_str, "%Y-%m-%d %H:%M")

    if direction == "1":
        # Время указано в Новосибирске, конвертируем в Москву
        local_time = novosibirsk_tz.localize(naive_time)
        converted_time = local_time.astimezone(moscow_tz)
        print(f"Время в Москве: {converted_time.strftime('%Y-%m-%d %H:%M')}")

    elif direction == "2":
        # Время указано в Москве, конвертируем в Новосибирск
        local_time = moscow_tz.localize(naive_time)
        converted_time = local_time.astimezone(novosibirsk_tz)
        print(f"Время в Новосибирске: {converted_time.strftime('%Y-%m-%d %H:%M')}")

    else:
        print("Неверный выбор направления.")
except ValueError:
    print("Ошибка ввода. Убедитесь, что формат времени: ГГГГ-ММ-ДД ЧЧ:ММ")


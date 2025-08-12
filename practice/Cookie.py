# Создаем программу просчета стоимости печенья и упаковки печенья.

def cookie(start_price):
    result_priсe = start_price + (start_price * (70 / 100))
    print(f"Стоимость одной печеньки с наценкой: {result_priсe}")
    return result_priсe

def pack_price(cookie_price, cookie_count):
    result_price = cookie_price * cookie_count + 57
    # 57 - стоимость упаковки
    return result_price

cookie_price = cookie(100)
pack = pack_price(cookie_price, 10)
print(f"Стоимость упаковки печенья с наценкой: {pack}")
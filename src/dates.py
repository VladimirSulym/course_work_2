import datetime


def get_date_for_filter() -> tuple:
    """Функция выдает приветствие, согласно текущему, времени и текущий месяц в который попадает текущая дата"""
    date_now = datetime.datetime.now()
    hour = date_now.hour
    if 0 <= hour < 6:
        greeting = "Доброй ночи"
    elif 6 <= hour < 12:
        greeting = "Доброе утро"
    elif 12 <= hour < 18:
        greeting = "Добрый день"
    elif 18 <= hour <= 24:
        greeting = "Добрый вечер"
    month_for_filter = date_now.month
    year_for_filter = date_now.year

    return greeting, month_for_filter, year_for_filter

def get_month_operation(date_str: str, month: int, year: int) -> bool:
    """Функция получает на вход строку даты для проверки и месяцу с годом. Выводит логический ответ True если
    дата входит в этот месяц и год"""
    date_operation = datetime.datetime.strptime(date_str, "%d.%m.%Y %H:%M:%S")
    if date_operation.month == month and date_operation.year == year:
        return True
    else:
        return False


if __name__ == "__main__":
    print(get_date_for_filter())
    print(get_month_operation())

import datetime
import logging

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
file_formatter = logging.Formatter("%(name)s / %(funcName)s / %(levelname)s: %(message)s")
console_handler.setFormatter(file_formatter)
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)


def get_date_for_filter(date) -> tuple:
    """Функция выдает приветствие, согласно текущему, времени и текущий месяц в который попадает текущая дата"""
    if date:
        date_now = date
    else:
        date_now = datetime.datetime.now()
    # logger.debug(date_now)
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


def str_to_date(date_str: str) -> datetime.date:
    # '%Y-%m-%d %H:%M:%S'
    logger.debug("Функция запущена")
    logger.debug(date_str)
    if date_str[2] == ".":
        logger.debug("Дата из DateFrame")
        return datetime.datetime.strptime(date_str, "%d.%m.%Y %H:%M:%S")
    else:
        logger.debug("Дата из ручного ввода")
        return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")


def get_month_operation(date_str: str, month: int, year: int) -> bool:
    """Функция получает на вход строку даты для проверки и месяцу с годом. Выводит логический ответ True если
    дата входит в этот месяц и год"""
    date_operation = str_to_date(date_str)
    if date_operation.month == month and date_operation.year == year:
        return True
    else:
        return False


# if __name__ == "__main__":
#     print(get_date_for_filter())
#     print(get_month_operation())

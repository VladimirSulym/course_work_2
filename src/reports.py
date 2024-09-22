import datetime
import logging
import os

import pandas as pd

from config import DATA_PATH
from src.utils import get_data_operations, spending_by_category

# Создаем логер с именем текущего модуля __name__
logger = logging.getLogger(__name__)
# Создаем хендлер для вывода в консоль
console_handler = logging.StreamHandler()
# Создаем форматер для форматирования вывода используемого хендлера
file_formatter = logging.Formatter("%(name)s / %(funcName)s / %(levelname)s: %(message)s")
# устанавливаем созданный форматер (file_formatter) для хендлера
console_handler.setFormatter(file_formatter)
# Прописываем хендлер в наш именной логер (logger)
logger.addHandler(console_handler)
# Устанавливаем необходимый уровень логера (DEBUG)
logger.setLevel(logging.INFO)
# Вывод лога в консоль
# logger.debug('Debug message')


def print_report(file_name=f'reports_{datetime.datetime.now().strftime("%d-%m-%Y %H_%M_%S")}.xlsx'):
    """Вспомогательная функция обертка"""

    def my_decorator(func):
        """Вспомогательная функция обертка"""

        def print_report_in_excel(*args, **kwargs):
            """Функция-декоратор, которая записывает результат работы функции в файл excel"""
            result = func(*args, **kwargs)
            result.to_excel(
                f"{os.path.join(DATA_PATH, file_name)}",
                index=False,
            )
            return result

        return print_report_in_excel

    return my_decorator


@print_report()
def set_spending_by_category(
    category="Супермаркеты", date_for_filter: datetime = datetime.datetime.now()
) -> pd.DataFrame:
    """Функция, которая принимает название категории и возвращает отфильтрованный DataFrame со всеми
    тратами по заданной категории за последние три месяца"""
    logger.info("Функция запущена")
    data_operations = get_data_operations()
    logger.debug("Получены данные из файла с операциями для дальнейшей обработки")
    result = spending_by_category(data_operations, category, date_for_filter).reset_index(drop=True)
    logger.info("Результат получен, функция успешно завершена")
    return result


# if __name__ == "__main__":
#     print(set_spending_by_category("Аптеки", datetime.datetime(2021, 12, 1, 00, 00, 00)))
#     print(set_spending_by_category("Супермаркеты"))

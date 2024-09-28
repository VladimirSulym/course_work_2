import datetime
import json
import logging
import os

import pandas as pd

from config import DATA_PATH
from src.dates import get_month_operation

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


def get_user_config() -> dict:
    """Функция, которая считывает конфигурацию пользователя из файла user_settings.json и
    возвращает словарь с параметрами"""
    with open(os.path.join(DATA_PATH, "user_settings.json"), "r") as f:
        data_user_config = json.load(f)
    return data_user_config


def get_data_operations() -> pd.DataFrame:
    """Функция считывает данные об операциях из файла operations.xlsx и возвращает из в виде DataFrame"""
    logger.info("Функция запущена")
    result = pd.read_excel(os.path.join(DATA_PATH, "operations.xlsx"))
    logger.info("Файл найден, данные извлечены без ошибок")
    return result


def get_data_operations_filter(data_operations: pd.DataFrame, month: int, years: int) -> pd.DataFrame:
    """Функция, которая принимает DataFrame и дату (месяц и год) для фильтрации и возвращает DataFrame
    отфильтрованный по дате"""
    logger.info("Функция запущена")
    data_operations_filter = data_operations[0:0]
    logger.debug("Создан временный DataFrame")
    for index, row in data_operations.iterrows():
        if get_month_operation(row["Дата операции"], month, years):
            logger.debug(f"Строка {index} подошла по условию")
            data_operations_filter = data_operations_filter._append(row, ignore_index=True)
            logger.debug(f"Строка {index} добавлена во временный DataFrame")
    logger.info("Функция завершена без ошибок")
    return data_operations_filter


def get_data_operations_group(data_operations: pd.DataFrame) -> list:
    """Функция, которая принимает DataFrame и группирует его по Номеру карты и получает сумму операций
    группированных карт"""
    logger.info("Функция запущена")
    data_operations_group = data_operations.groupby("Номер карты").agg({"Сумма операции с округлением": ["sum"]})
    logger.debug(
        'DataFrame сгруппирован по столбцу "Номер карты" и просуммирован по столбцу "Сумма операции с округлением"'
    )
    result = []
    for index, row in data_operations_group.iterrows():
        result.append(
            {
                "last_digits": index[-4:],
                "total_spent": round(float(row.loc["Сумма операции с округлением"].values[0]), 2),
                "cashback": round(float(row.loc["Сумма операции с округлением"].values[0]) / 100, 2),
            }
        )
        logger.debug(f"Добавлена карта {index} в результат списка")
    logger.info("Функция завершена без ошибок")
    return result


def counts_top_transactions(data_operations: pd.DataFrame) -> list:
    """Формирует ТОП 5 транзакций по сумме платежа"""
    logger.info("Функция запущена")
    data_operations.sort_values("Сумма платежа", ascending=True, inplace=True)
    result = []
    for index, row in data_operations.iloc[0:5].iterrows():
        result.append(
            {
                "date": row["Дата платежа"],
                "amount": row["Сумма платежа"],
                "category": row["Категория"],
                "description": row["Описание"],
            }
        )
    logger.info("Функция завершена без ошибок")
    return result


def prof_categories_cashback(data_operations: pd.DataFrame, month: int, years: int) -> object:
    """Функция определяет сколько кэшбека заработано в отчетный период (месяц) по всем категориям"""
    logger.info("Функция запущена")
    data_operations_filter = get_data_operations_filter(data_operations, month, 2021)
    data_operations_group = data_operations_filter.groupby("Категория").agg({"Кэшбэк": ["sum"]})
    result = {}
    for index, row in data_operations_group.iterrows():
        result.update({index: int(row.loc["Кэшбэк"].values[0])})
    logger.info("Функция завершена без ошибок")
    return result


def spending_by_category(data_operations: pd.DataFrame, category: str, date: datetime):
    """Функция получает на вход дата фрейма категорию и дату для фильтрации и возвращает все расходы по данной
    категории за последние три месяца от заодно этот"""
    logger.info("Функция запущена")
    dates_range_for_filter = []
    if date.year > 2021:
        date = date.replace(year=2021)
    for i in (0, 30, 30):
        date = date - datetime.timedelta(days=i)
        dates_range_for_filter.append([date.month, date.year])
    data_operations_filter = data_operations[0:0]
    for date_range_for_filter in dates_range_for_filter:
        data_operations_filter = data_operations_filter._append(
            get_data_operations_filter(data_operations, date_range_for_filter[0], date_range_for_filter[1]),
            ignore_index=True,
        )
    result = data_operations_filter.loc[
        (data_operations_filter["Категория"] == category) & (data_operations_filter["Сумма операции"] < 0)
    ]
    logger.info("Функция завершена без ошибок")
    return result


# if __name__ == "__main__":
#     data_operations_filter = get_data_operations_filter(get_data_operations(), 10, 2021)

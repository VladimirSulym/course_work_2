import datetime
import os

import pandas as pd

from config import DATA_PATH
from src.utils import get_data_operations, spending_by_category


def print_report(file_name=f'reports_{datetime.datetime.now().strftime("%d-%m-%Y %H_%M_%S")}.xlsx'):
    def my_decorator(func):
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
    """Функция, которая принимает название категории и возвращает отфильтрованной DataFrame со всеми
    тратами по заданной категории за последние три месяца"""
    data_operations = get_data_operations()
    result = spending_by_category(data_operations, category, date_for_filter).reset_index(drop=True)
    return result


if __name__ == "__main__":
    # print(set_spending_by_category("Аптеки", datetime.datetime(2021, 12, 1, 00, 00, 00)))
    print(set_spending_by_category("Супермаркеты"))

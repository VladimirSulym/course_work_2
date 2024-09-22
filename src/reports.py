import datetime

import pandas as pd

from src.utils import get_data_operations, spending_by_category


def print_report(func):
    def print_report_in_file():
        result = func()
        return result
    return print_report_in_file

@print_report
def set_spending_by_category(category = 'Супермаркеты') -> pd.DataFrame:
    data_operations = get_data_operations()
    date_for_filter = datetime.datetime(2021, 1, 12, 00, 00, 00)
    result = spending_by_category(data_operations, category, date_for_filter)
    return result


if __name__ == '__main__':
    print(set_spending_by_category())

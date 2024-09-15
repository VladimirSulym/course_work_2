import json
import os

import pandas as pd

from config import DATA_PATH
from src.dates import get_month_operation


def get_user_config():
    with open(os.path.join(DATA_PATH, "user_settings.json"), "r") as f:
        data_user_config = json.load(f)
    return data_user_config


def get_data_operations() -> pd.DataFrame:
    return pd.read_excel(os.path.join(DATA_PATH, "operations.xlsx"))


if __name__ == "__main__":
    # print(get_user_config())
    # print(get_data_operations())
    data_operations = get_data_operations()
    # print(data_operations)
    data_operations_filter = pd.DataFrame()

    for index, row in data_operations.iterrows():
        if get_month_operation(row['Дата операции'], 10, 2021):
            data_operations_filter = data_operations_filter._append(row, ignore_index=True)
    print(data_operations_filter)

    print(data_operations_filter.columns)


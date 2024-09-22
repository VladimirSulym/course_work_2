import json
import os

from config import DATA_PATH, SET_DATA
from src.dates import get_date_for_filter
from src.utils import get_data_operations, prof_categories_cashback


def set_prof_categories_cashback():
    data_operations = get_data_operations()
    date_for_filter = get_date_for_filter()
    return prof_categories_cashback(data_operations, date_for_filter[1], date_for_filter[2])


if __name__ == "__main__":
    print(set_prof_categories_cashback())
    prof_categories_cashback = set_prof_categories_cashback()

    with open(os.path.join(DATA_PATH, "set_data_services.json"), "w") as f:
        json.dump(prof_categories_cashback, f, ensure_ascii=False, sort_keys=False, indent=4)

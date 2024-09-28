import json

from src.dates import get_date_for_filter, str_to_date
from src.utils import get_data_operations, prof_categories_cashback


def set_prof_categories_cashback(date):
    """Функция, которая собирает данные сколько на каждой категории можно заработать кешбэка в указанном месяце года
    и передает их в JSON"""
    data_operations = get_data_operations()
    date_for_filter = get_date_for_filter(str_to_date(date))

    result = prof_categories_cashback(data_operations, date_for_filter[1], date_for_filter[2])

    # with open(os.path.join(DATA_PATH, "set_data_services.json"), "w") as f:
    #     json.dump(result, f, ensure_ascii=False, sort_keys=False, indent=4)

    result = json.dumps(result, ensure_ascii=False, sort_keys=False, indent=4)

    return result


# if __name__ == "__main__":
#     print(set_prof_categories_cashback())
#     print(set_prof_categories_cashback())

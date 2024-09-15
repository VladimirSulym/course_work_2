from src.api_requests import get_data_request_curr_stock
from src.dates import get_date_for_filter
import json
import os
from config import DATA_PATH, SET_DATA
from src.utils import get_data_operations, get_data_operations_filter, get_data_operations_group, \
    counts_top_transactions, get_user_config


def set_viewer_main_page():
    date_for_filter = get_date_for_filter()
    print(date_for_filter)
    SET_DATA["greeting"] = date_for_filter[0]
    data_operations = get_data_operations()
    # data_operations_filter = get_data_operations_filter(data_operations,  date_for_filter[1],  date_for_filter[2])
    data_operations_filter = get_data_operations_filter(data_operations,  11,  2021)
    SET_DATA['cards'] = get_data_operations_group(data_operations_filter)
    SET_DATA['top_transactions'] = counts_top_transactions(data_operations_filter)

    data_currencies = []
    for i in get_user_config()['user_currencies']:
        data_currencies.append({
            'currency': i,
            'rate': get_data_request_curr_stock(i)
        })
    SET_DATA['currency_rates'] = data_currencies

    with open(os.path.join(DATA_PATH, "set_data.json"), "w") as f:
        json.dump(SET_DATA, f, ensure_ascii=False, sort_keys=False, indent=4)

    print(SET_DATA)


if __name__ == "__main__":
    set_viewer_main_page()

from src.dates import get_date_for_filter
import json
import os
from config import DATA_PATH, SET_DATA


def set_viewer_main_page():
    SET_DATA["greeting"] = get_date_for_filter()[0]
    with open(os.path.join(DATA_PATH, "set_data.json"), "w") as f:
        json.dump(SET_DATA, f, ensure_ascii=False, sort_keys=False, indent=4)


    print(SET_DATA)


if __name__ == "__main__":
    set_viewer_main_page()

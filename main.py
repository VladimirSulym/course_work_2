import datetime

from src.reports import set_spending_by_category
from src.services import set_prof_categories_cashback
from src.views import set_viewer_main_page


def main():
    print(set_viewer_main_page())
    print(set_prof_categories_cashback())
    print(set_spending_by_category("Супермаркеты", datetime.datetime(2021, 8, 1, 00, 00, 00)))


if __name__ == '__main__':
    main()

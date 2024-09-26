from src.dates import str_to_date
from src.reports import set_spending_by_category
from src.services import set_prof_categories_cashback
from src.views import set_viewer_main_page


def main():
    main_date_str = input("Введите дату в формате YYYY-MM-DD HH:MM:SS => ")
    print(set_viewer_main_page(main_date_str))
    print(set_prof_categories_cashback(main_date_str))
    print(set_spending_by_category("Супермаркеты", str_to_date(main_date_str)))


if __name__ == "__main__":
    main()

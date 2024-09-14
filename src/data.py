import datetime


def get_date_for_filter():
    date_now = datetime.datetime.now()
    # hour = date_now.hour
    hour = 12
    if 0 <= hour < 6:
        greeting = 'Доброй ночи'
    elif 6 <= hour < 12:
        greeting = 'Доброе утро'
    elif 12 <= hour < 18:
        greeting = 'Добрый день'
    elif 18 <= hour <= 24:
        greeting = 'Добрый вечер'

    month_for_filter = date_now.month

    return greeting, month_for_filter

if __name__ == '__main__':
    print(get_date_for_filter())
import datetime
from unittest.mock import patch

import pytest

from src.dates import get_date_for_filter, get_month_operation, str_to_date


@pytest.mark.parametrize(
    "hour, expected",
    [
        (11, "Доброе утро"),
        (4, "Доброй ночи"),
        (14, "Добрый день"),
        (19, "Добрый вечер"),
    ],
)
@patch("datetime.datetime")
def test_dates_1(mock_datetime, hour, expected):
    mock_datetime.now.return_value.hour = hour
    mock_datetime.now.return_value.month = 1
    mock_datetime.now.return_value.year = 2020
    assert get_date_for_filter(None) == (expected, 1, 2020)


@pytest.mark.parametrize(
    "date, expected",
    [
        (datetime.datetime(2021, 11, 12, 11, 12, 12), "Доброе утро"),
        (datetime.datetime(2021, 11, 12, 4, 12, 12), "Доброй ночи"),
        (datetime.datetime(2021, 11, 12, 14, 12, 12), "Добрый день"),
        (datetime.datetime(2021, 11, 12, 19, 12, 12), "Добрый вечер"),
    ],
)
def test_dates_2(date, expected):
    assert get_date_for_filter(date) == (expected, 11, 2021)


@pytest.mark.parametrize(
    "date_str, month, year, expected",
    [
        ("11.12.2021 12:12:12", 11, 2021, False),
        ("11.11.2021 10:10:32", 11, 2021, True),
    ],
)
def test_get_month_operation(date_str, month, year, expected):
    assert get_month_operation(date_str, month, year) == expected


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("11.12.2021 12:12:12", datetime.datetime.strptime("11.12.2021 12:12:12", "%d.%m.%Y %H:%M:%S")),
        ("2021-11-12 12:12:12", datetime.datetime.strptime("2021-11-12 12:12:12", "%Y-%m-%d %H:%M:%S")),
    ],
)
def test_str_to_date(date_str, expected):
    assert str_to_date(date_str) == expected

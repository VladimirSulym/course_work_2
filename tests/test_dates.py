import pytest

from src.dates import get_date_for_filter, get_month_operation
from unittest.mock import patch


@pytest.mark.parametrize('hour, expected', [
    (11, 'Доброе утро'),
    (4, 'Доброй ночи'),
    (14, 'Добрый день'),
    (19, 'Добрый вечер'),
])
@patch('datetime.datetime')
def test_dates(mock_datetime, hour, expected):
    mock_datetime.now.return_value.hour = hour
    mock_datetime.now.return_value.month = 1
    mock_datetime.now.return_value.year = 2020
    assert get_date_for_filter() == (expected, 1, 2020)


@pytest.mark.parametrize(
    'date_str, month, year, expected',
    [('11.12.2021 12:12:12', 11, 2021, False),
     ('11.11.2021 10:10:32', 11, 2021, True),
     ],
)
def test_get_month_operation(date_str, month, year, expected):
    assert get_month_operation(date_str, month, year) == expected

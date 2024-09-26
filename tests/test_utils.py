from unittest.mock import patch

import pandas as pd
import pytest
from pandas._testing import assert_frame_equal

from src.utils import (counts_top_transactions, get_data_operations,
                       get_data_operations_filter, get_data_operations_group,
                       get_user_config)


@pytest.fixture
def my_fixture():
    return pd.DataFrame()


@patch("json.load")
def test_get_user_config(mock_load):
    mock_load.return_value = {}
    assert get_user_config() == {}
    mock_load.assert_called_once()


@patch("pandas.read_excel")
def test_get_data_operations(mock_read):
    mock_read.return_value = {}
    assert get_data_operations() == {}
    mock_read.assert_called_once()


@patch("src.dates.get_month_operation")
def test_get_data_operations_filter(mock_get_month, my_fixture):
    mock_get_month.return_value = my_fixture
    assert_frame_equal(get_data_operations_filter(pd.DataFrame(), 1, 2021), my_fixture)


@patch("pandas.DataFrame.groupby")
def test_get_data_operations_groupby(mock_group, my_fixture):
    mock_group.return_value.iterrows.return_value = my_fixture
    assert get_data_operations_group(my_fixture) == []
    mock_group.assert_called_once_with("Номер карты")


@patch("pandas.DataFrame.sort_values")
def test_counts_top_transactions(mock_sort, my_fixture):
    mock_sort.return_value = my_fixture
    assert counts_top_transactions(my_fixture) == []
    mock_sort.assert_called_once()

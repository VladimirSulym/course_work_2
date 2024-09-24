from unittest.mock import patch

from src.services import set_prof_categories_cashback
from pandas.testing import assert_frame_equal

@patch("src.utils.prof_categories_cashback")
@patch("src.dates.get_date_for_filter")
@patch("src.utils.get_data_operations")
def test_set_prof_categories_cashback(mock_get_data_operations, mock_get_date_for_filter, mock_prof_categories_cashback):
    mock_get_data_operations.return_value = []
    mock_get_date_for_filter.return_value = "2020-01-01"
    mock_prof_categories_cashback.return_value.json.dumps.return_value = 10
    # assert set_prof_categories_cashback() == 10
    assert_frame_equal(set_prof_categories_cashback(), 10)
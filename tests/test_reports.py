from unittest.mock import patch

from pandas._testing import assert_frame_equal

from src.reports import set_spending_by_category

@patch('src.utils.spending_by_category')
@patch('src.utils.get_data_operations')
def test_set_spending_by_category(mock_get_data_operations, mock_spending_by_category):
    mock_get_data_operations.return_value = 1
    mock_spending_by_category.return_value.reset_index.return_value = 1
    # assert set_spending_by_category("Супермаркеты") == 1
    assert_frame_equal(set_spending_by_category("Супермаркеты"), 1)

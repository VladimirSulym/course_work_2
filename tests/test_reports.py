from unittest.mock import patch

import pandas as pd
from pandas._testing import assert_frame_equal

from src.reports import set_spending_by_category


@patch("pandas.DataFrame.reset_index")
@patch("src.utils.get_data_operations")
def test_set_spending_by_category(mock_get_data_operations, mock_reset_index):
    mock_get_data_operations.return_value = 1
    mock_reset_index.return_value = pd.DataFrame()
    # assert set_spending_by_category("Супермаркеты") == pd.DataFrame()
    assert_frame_equal(set_spending_by_category("Супермаркеты"), pd.DataFrame())

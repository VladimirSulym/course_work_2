from unittest.mock import patch

from src.api_requests import get_data_request_curr_stock, get_data_request_curr_trade

@patch('requests.get')
def test_get_data_request_curr_stock(mock_get):
    mock_get.return_value.json.return_value = {"result": 10.00}
    assert get_data_request_curr_stock('EUR') == 10.00


@patch('requests.get')
def test_get_data_request_curr_trade(mock_get):
    mock_get.return_value.json.return_value = {"data": [{'close': 10.00}]}
    assert get_data_request_curr_trade('AAPL') == 10.00
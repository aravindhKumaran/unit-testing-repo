import pytest 
import source.service as service
import unittest.mock as mock 
import requests


# Using unit test to create mock
@mock.patch("source.service.get_user_from_db")  # path to the actual function 
def test_get_user_from_db(mock_get_user_from_db):
    # Assemble
    mock_get_user_from_db.return_value = "Alice"
    
    # Act: calling the function
    user_name = service.get_user_from_db(2)

    # Assert
    assert user_name == "Alice"


# We are mocking the requests.get() function within get_users_api_call()
@mock.patch("requests.get")
def test_get_users_api_call(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}
    mock_get.return_value = mock_response 

    data = service.get_users_api_call()
    assert data == {"id": 1, "name": "John Doe"}


@mock.patch("requests.get")
def test_get_users_api_call_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response

    with pytest.raises(requests.HTTPError):
        service.get_users_api_call()

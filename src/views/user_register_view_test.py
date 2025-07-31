import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .user_register_view import UserRegisterView

class MockController:
    def registry(self, username, password):
        return { "alguma": "coisa" }
    
def test_handle_user_register():
    body = {
        "username": "MyUsername",
        "password": "MyPassword"
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    response = user_register_view.handle(request)
    # print()
    # print(response)
    # print(response.body)

    assert isinstance(response, HttpResponse)
    assert response.body == {'data': {'alguma': 'coisa'}}
    assert response.status_code == 201

def test_handle_user_register_with_validation_error():
    body = {
        "password": "MyPassword"
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    with pytest.raises(Exception):
       user_register_view.handle(request)

# pytest -s -v src/views/user_register_view_test.py
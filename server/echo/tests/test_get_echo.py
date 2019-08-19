from datetime import  datetime
from echo.controllers import get_echo


def test_get_echo():
    action_name = 'echo'
    data = 'Some data'

    request = {
        'actions': action_name,
        'time': datetime.now().timestamp(),
        'data': data,
    }

    expected = {
        'actions': action_name,
        'user': None,
        'time': None,
        'data': data,
        'code': 200,
    }

    response = get_echo(request)

    assert response.get('data') == expected.get('data')

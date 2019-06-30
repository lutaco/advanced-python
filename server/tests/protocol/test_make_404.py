import pytest
from datetime import datetime
from protocol import make_404


@pytest.fixture
def action():
    return 'some_action'


@pytest.fixture
def user():
    return 'some_user'


@pytest.fixture
def time():
    return datetime.now().timestamp()


@pytest.fixture
def ret_code():
    return 404


@pytest.fixture
def valid_request(action, user, time):
    return {
        'action': action,
        'user': user,
        'time': time,
    }


def test_make_400(valid_request, ret_code):

    response = make_404(valid_request)

    assert response.get('code') == ret_code

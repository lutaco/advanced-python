import pytest
from datetime import datetime
from protocol import validate_request


@pytest.fixture
def action():
    return 'some_action'


@pytest.fixture
def time():
    return datetime.now().timestamp()


@pytest.fixture
def valid_raw(action, time):
    return {
        'action': action,
        'time': time,
}


@pytest.fixture
def not_valid_raw(action, time):
    return {
        'action': action,
        'time': None,
    }


def test_validate_request(valid_raw, not_valid_raw):

    assert validate_request(valid_raw) is True
    assert validate_request(not_valid_raw) is False


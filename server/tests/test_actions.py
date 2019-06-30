import pytest
from actions import resolve


@pytest.fixture
def valid_action_name():
    return 'some_action'


@pytest.fixture
def not_valid_action_name():
    return 'another_action'


@pytest.fixture
def controller():
    return 'some_controller'


@pytest.fixture
def actions(valid_action_name, controller):
    return [{
        'actions': valid_action_name,
        'controller': controller,
    }]


def test_resolve(valid_action_name, not_valid_action_name, controller, actions):

    res_controllers = [
        resolve(valid_action_name, actions),
        resolve(not_valid_action_name, actions)
    ]

    expected = [
        controller,
        None
    ]

    for i, item in enumerate(res_controllers):
        assert item == expected[i]


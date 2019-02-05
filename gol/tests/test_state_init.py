from mock import patch
from gol.state_init import null_state, random_state

def test_null_state():
    width = 3
    height = 3
    expected_state = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    result = null_state(width, height)

    assert result == expected_state

@patch('gol.state_init.random.randint')
def test_random_state(randint_mock):
    randint_mock.side_effect = [0, 1, 0] * 3

    width = 3
    height = 3

    expected_state = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]

    state = random_state(width, height)

    assert state == expected_state

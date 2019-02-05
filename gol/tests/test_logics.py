from gol.logics import (
    cell_neighbors,
    next_cell_state,
    next_state
)


def test_cell_neighbors():
    state = [
        [0, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 1, 0]
    ]

    points = [
        (0, 0),
        (1, 1),
        (3, 3)
    ]

    results = [
        [1, 1, 0],
        [0, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1]
    ]

    for idx, point in enumerate(points):
        neighbors = cell_neighbors(state, point)

        assert neighbors == results[idx]


def test_next_cell_state():
    # 5 lives - overpopulation -> kill
    state = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 1, 1]
    ]

    point = (1, 1)

    new_state = next_cell_state(state, point)

    assert new_state == 0

    # 3 lives - underpopulation -> live
    state = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 0]
    ]

    point = (1, 1)

    new_state = next_cell_state(state, point)

    assert new_state == 1

    # 2 lives - underpopulation -> nothing
    state = [
        [0, 0, 1],
        [0, 0, 0],
        [1, 0, 0]
    ]

    point = (1, 1)

    new_state = next_cell_state(state, point)

    assert new_state == 0


def test_next_state():
    # Oscillator test
    state = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    expected_state = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    new_state = next_state(state)

    assert new_state == expected_state

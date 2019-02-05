import random
from typing import List, Tuple

State = List[List[int]]
Point = Tuple[int, int]


def null_state(width: int, height: int) -> State:
    """
    Create zero state with all cells are dead.

    :param int width: width of state
    :param int height: height of state

    :return: zero state
    :rtype: List[List[int]]
    """
    result : State = [
        [0 for _ in range(width)] for _ in range(height)
    ]

    return result


def random_state(width: int, height: int) -> State:
    """
    Create random state.

    :param int width: width of state
    :param int height: height of state

    :return: random state
    :rtype: List[List[int]]
    """

    default = null_state(width, height)

    for x in range(height):
        for y in range(width):
            default[x][y] = random.randint(0, 1)

    return default

"""
Module wich represents main logics of Conway Game of Life
"""
import copy
from typing import List, Tuple

Point = Tuple[int, int]
State = List[List[int]]


def next_state(state: State) -> State:
    """
    Generates next state of cellular automate

    :param state: current state
    :type state: List[List[int]]

    :return: Next state
    :rtype: List[List[int]]
    """
    new_state = copy.deepcopy(state)

    for i in range(len(state)):
        for j in range(len(state[0])):
            new_state[i][j] = next_cell_state(state, (i, j))

    return new_state


def next_cell_state(state: State, point: Point) -> int:
    """
    Calculates next cell state (main logics of cellular automate)

    :param state: current state
    :type state: List[List[int]]

    :param point: Point to current cell
    :type point: Tuple[int, int]

    :return: Next cell state depends of cell neighbors
    :rtype: int
    """
    live_neighbors = [x for x in cell_neighbors(state, point) if x]

    lives = len(live_neighbors)

    x_point, y_point = point
    cell_state = state[x_point][y_point]

    if cell_state == 1 and (lives < 2 or lives > 3):
        return 0

    if (cell_state == 1 and lives >= 2) or (cell_state == 0 and lives == 3):
        return 1

    return cell_state


def cell_neighbors(state: State, point: Point, width: int = 1) -> List[int]:
    """
    Loads all values of cell neighbors and returns it's as a list

    :param state: current state
    :type state: List[List[int]]

    :param point: Point to current cell
    :type point: Tuple[int, int]

    :param int width: width of cell neighbors square

    :return: List of neighbor values
    :rtype: List[int]
    """
    result = []
    x_point, y_point = point

    for row in range(x_point - width, x_point + width + 1):
        for column in range(y_point - width, y_point + width + 1):
            if row < 0 or column < 0:
                continue

            if row >= len(state) or column >= len(state[0]):
                continue

            if row == x_point and column == y_point:
                continue

            result.append(state[row][column])

    return result

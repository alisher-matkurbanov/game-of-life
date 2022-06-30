import random
from typing import List

Grid = List[List[int]]


def print_grid(grid: Grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end="  ")
        print()
    print()


def count_alive_neighbours(cur_row: int, cur_col: int, state: Grid) -> int:
    row_len = len(state[0])
    col_len = len(state)
    assert row_len == col_len
    assert row_len > 0
    alive_neighbours = 0
    # check upper row
    if cur_row - 1 >= 0:
        alive_neighbours += state[cur_row - 1][cur_col]
        if cur_col - 1 >= 0:
            alive_neighbours += state[cur_row - 1][cur_col - 1]
        if cur_col + 1 < row_len:
            alive_neighbours += state[cur_row - 1][cur_col + 1]
    # check current row
    if cur_col - 1 >= 0:
        alive_neighbours += state[cur_row][cur_col - 1]
    if cur_col + 1 < row_len:
        alive_neighbours += state[cur_row][cur_col + 1]
    # check lower row
    if cur_row + 1 < col_len:
        alive_neighbours += state[cur_row + 1][cur_col]
        if cur_col - 1 >= 0:
            alive_neighbours += state[cur_row + 1][cur_col - 1]
        if cur_col + 1 < row_len:
            alive_neighbours += state[cur_row + 1][cur_col + 1]

    return alive_neighbours


def compute_next_state(state: Grid):
    assert len(state[0]) == len(state)
    row_len = len(state[0])
    col_len = len(state)
    new_state = [[0 for _ in range(row_len)] for _ in range(col_len)]
    for i in range(col_len):
        for j in range(row_len):
            alive_around = count_alive_neighbours(i, j, state)
            if state[i][j] == 1:
                new_state[i][j] = int(alive_around in (2, 3))
            # reproduction
            if state[i][j] == 0:
                new_state[i][j] = int(alive_around == 3)
    return new_state


def generate_grid(size: int) -> Grid:
    g = []
    for i in range(size):
        g.append([])
        for j in range(size):
            g[i].append(random.randint(0, 1))
    return g


if __name__ == "__main__":
    init_state = generate_grid(1000)
    # print_grid(init_state)

    state = compute_next_state(init_state)
    # print_grid(state)

    state = compute_next_state(state)
    # print_grid(state)

    state = compute_next_state(state)
    # print_grid(state)

    state = compute_next_state(state)
    # print_grid(state)

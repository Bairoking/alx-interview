#!/usr/bin/python3
"""Island Perimeter"""


def check_val(s):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if (s == 0):
        return 1
    return 0


def island_perimeter(grid):
    """_summary_

    Args:
        grid (_type_): _description_
    """

    row = len(grid)
    col = len(grid[0])
    assert (1 <= row and col <= 100), "length must be between 1 an 100"

    s = 0
    for i in range(row):
        for j in range(col):
            assert (grid[i][j] == 0) or (grid[i][j] == 1),\
                "grid numbers must be 0 or 1"
            if grid[i][j] == 1:
                if i-1 < 0:
                    s += 1
                else:
                    s += check_val(grid[i-1][j])
                if j-1 < 0:
                    s += 1
                else:
                    s += check_val(grid[i][j-1])

                try:
                    s += check_val(grid[i+1][j])
                except IndexError:
                    s += 1
                try:
                    s += check_val(grid[i][j+1])
                except IndexError:
                    s += 1

    return s

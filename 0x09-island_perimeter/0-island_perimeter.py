#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """Returns perimeter of island"""
    height = len(grid)
    width = len(grid[0])
    count = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                count += 4

                if i > 0 and grid[i - 1][j] == 1:
                    count -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    count -= 2

    return count

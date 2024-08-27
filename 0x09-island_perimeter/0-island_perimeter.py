#!/usr/bin/python3
"""
Module to calculate the perimeter of the island
"""

def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Assume the cell is completely surrounded by water, so add 4 to the perimeter
                perimeter += 4

                # Check the cell above (if it's land, subtract 2 from the perimeter)
                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 2

                # Check the cell to the left (if it's land, subtract 2 from the perimeter)
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 2

    return perimeter


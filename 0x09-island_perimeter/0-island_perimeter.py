#!/usr/bin/python3
"""
Function to calculate the perimeter of the island described in the grid
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.
    
    Args:
        grid (list of list of int): A grid representing the map, where 0 is water and 1 is land.
    
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Assume each land cell has 4 sides
                perimeter += 4

                # Check if there's land on the left (adjacent)
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Remove 2 sides for shared border with left cell

                # Check if there's land above (adjacent)
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Remove 2 sides for shared border with top cell

    return perimeter

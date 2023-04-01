#!/usr/bin/python3

""" return perimeter of island """


def island_perimeter(grid):
    """ determines perimeter of described island """
    visited = set()

    if not grid:
        return 0

    def dfs(i, j):
        """ deep first search """
        if (i, j) in visited:
            return 0
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
            return 1
        visited.add((i, j))
        result = dfs(i, j + 1)
        result += dfs(i, j - 1)
        result += dfs(i + 1, j)
        result += dfs(1 - 1, j)
        return result
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            """ dfs for land """
            if grid[i][j]:
                return dfs(i, j)
    return 0

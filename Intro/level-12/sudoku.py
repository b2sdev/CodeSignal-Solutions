def solution(grid):
    for row in grid:
        row_set = set(row)
        if len(row_set) != 9:
            return False
        if sum(row) != 45:
            return False
    for c in range(9):
        col = []
        for r in range(9):
            col.append(grid[r][c])
        if sum(col) != 45:
            return False
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            sub_grid = []
            for i in range(3):
                sub_grid.extend(grid[r + i][c : c + 3])
            if sum(sub_grid) != 45:
                return False
    return True


grid = [
    [1, 3, 2, 5, 4, 6, 9, 8, 7],
    [4, 6, 5, 8, 7, 9, 3, 2, 1],
    [7, 9, 8, 2, 1, 3, 6, 5, 4],
    [9, 2, 1, 4, 3, 5, 8, 7, 6],
    [3, 5, 4, 7, 6, 8, 2, 1, 9],
    [6, 8, 7, 1, 9, 2, 5, 4, 3],
    [5, 7, 6, 9, 8, 1, 4, 3, 2],
    [2, 4, 3, 6, 5, 7, 1, 9, 8],
    [8, 1, 9, 3, 2, 4, 7, 6, 5],
]
assert solution(grid) == True

grid = [
    [1, 3, 4, 2, 5, 6, 9, 8, 7],
    [4, 6, 8, 5, 7, 9, 3, 2, 1],
    [7, 9, 2, 8, 1, 3, 6, 5, 4],
    [9, 2, 3, 1, 4, 5, 8, 7, 6],
    [3, 5, 7, 4, 6, 8, 2, 1, 9],
    [6, 8, 1, 7, 9, 2, 5, 4, 3],
    [5, 7, 6, 9, 8, 1, 4, 3, 2],
    [2, 4, 5, 6, 3, 7, 1, 9, 8],
    [8, 1, 9, 3, 2, 4, 7, 6, 5],
]
assert solution(grid) == False

grid = [
    [5, 5, 5, 5, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 5, 5, 5, 5],
]
assert solution(grid) == False

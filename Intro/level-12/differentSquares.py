def solution(matrix):
    h, w = len(matrix), len(matrix[0])
    squares_set = set()
    for r in range(0, h - 1):
        for c in range(0, w - 1):
            squares_set.add(tuple(matrix[r][c : c + 2] + matrix[r + 1][c : c + 2]))
    return len(squares_set)


matrix = [[1, 2, 1], [2, 2, 2], [2, 2, 2], [1, 2, 3], [2, 2, 1]]
assert solution(matrix) == 6

def solution(matrix):
    def update(mines, row, col):
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r == row and c == col:
                    continue
                if 0 <= r < len(mines) and 0 <= c < len(mines[0]):
                    mines[r][c] += 1

    mines = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == True:
                update(mines, row, col)
    return mines


matrix = [[True, False, False], [False, True, False], [False, False, False]]
assert solution(matrix) == [[1, 2, 1], [2, 1, 1], [1, 1, 1]]

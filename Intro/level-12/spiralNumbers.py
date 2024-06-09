def solution(n):
    num = 1
    dir = 0  # ['right', 'down', 'left', 'up']
    row, col = 0, 0
    matrix = [[0] * n for _ in range(n)]

    while num <= n * n:
        if dir == 0:
            while col < n and matrix[row][col] == 0:
                matrix[row][col] = num
                num += 1
                col += 1
            col -= 1
            row += 1
            dir = 1
        elif dir == 1:
            while row < n and matrix[row][col] == 0:
                matrix[row][col] = num
                num += 1
                row += 1
            row -= 1
            col -= 1
            dir = 2
        elif dir == 2:
            while col >= 0 and matrix[row][col] == 0:
                matrix[row][col] = num
                num += 1
                col -= 1
            col += 1
            row -= 1
            dir = 3
        elif dir == 3:
            while row >= 0 and matrix[row][col] == 0:
                matrix[row][col] = num
                num += 1
                row -= 1
            row += 1
            col += 1
            dir = 0

    return matrix


assert solution(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

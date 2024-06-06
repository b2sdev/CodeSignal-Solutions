def solution(image):
    def oper(row, col):
        pixel = []
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                pixel.append(image[r][c])
        return sum(pixel) // 9

    result = []
    for row in range(len(image) - 2):
        new_row = []
        for col in range(len(image[0]) - 2):
            new_row.append(oper(row, col))
        result.append(new_row)
    return result


assert solution([[1, 1, 1], [1, 7, 1], [1, 1, 1]]) == [[1]]
assert solution([[7, 4, 0, 1], [5, 6, 2, 2], [6, 10, 7, 8], [1, 4, 2, 0]]) == [
    [5, 4],
    [4, 4],
]
assert solution([[36, 0, 18, 9], [27, 54, 9, 0], [81, 63, 72, 45]]) == [[40, 30]]

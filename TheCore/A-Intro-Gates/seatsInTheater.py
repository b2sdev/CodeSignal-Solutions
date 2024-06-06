def solution(nCols, nRows, col, row):
    return (nCols - col + 1) * (nRows - row)


assert solution(16, 11, 5, 3) == 96

def solution1(a):
    size = len(a)
    res = [[0] * size for _ in range(size)]
    for r in range(size):
        for c in range(size):
            res[c][size - 1 - r] = a[r][c]
    return res


def solution(a):
    N = len(a)
    for r in range(0, N):
        for c in range(0, r):
            temp = a[r][c]
            a[r][c] = a[c][r]
            a[c][r] = temp
    for r in range(0, N):
        for c in range(0, N // 2):
            temp = a[r][c]
            a[r][c] = a[r][N - 1 - c]
            a[r][N - 1 - c] = temp
    return a


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert solution(a) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

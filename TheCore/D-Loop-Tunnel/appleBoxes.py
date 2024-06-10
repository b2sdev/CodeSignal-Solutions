def solution(k):
    red, yellow = 0, 0
    for size in range(1, k + 1):
        if size % 2 == 0:
            red += size * size
        else:
            yellow += size * size
    return red - yellow


assert solution(5) == -15

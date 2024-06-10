def solution(n, m):
    return ~(n ^ m) & -(~(n ^ m))


assert solution(10, 11) == 2

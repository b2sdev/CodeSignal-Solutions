def solution(n, k):
    return n & ~(1 << k - 1)


assert solution(37, 3) == 33
assert solution(37, 4) == 37

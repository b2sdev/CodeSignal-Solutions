def solution(n):
    factorial = 1
    k = 2
    while factorial < n:
        factorial *= k
        k += 1
    return factorial


assert solution(17) == 24

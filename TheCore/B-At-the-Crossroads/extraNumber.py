def solution(a, b, c):
    if a == b:
        return c
    elif a == c:
        return b
    else:
        return a


assert solution(2, 7, 2) == 7

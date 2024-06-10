def solution(n):
    return 2 ** bin(n)[2:][::-1].find("0", bin(n)[2:][::-1].find("0") + 1)


assert solution(37) == 8
assert solution(1073741824) == 2

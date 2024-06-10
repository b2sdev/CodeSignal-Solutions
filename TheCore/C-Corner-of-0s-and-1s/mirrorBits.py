def solution(a):
    return int(bin(a)[2:][::-1], 2)


assert solution(97) == 67
assert solution(8) == 1

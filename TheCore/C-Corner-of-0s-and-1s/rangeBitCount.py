def solution(a, b):
    s = "".join([bin(n)[2:] for n in range(a, b + 1)])
    return s.count("1")


assert solution(2, 7) == 11
assert solution(0, 1) == 1

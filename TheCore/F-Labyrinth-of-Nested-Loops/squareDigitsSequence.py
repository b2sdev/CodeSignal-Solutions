def solution(a0):
    seen = set()
    a = a0
    while a not in seen:
        seen.add(a)
        a = sum(int(digit) ** 2 for digit in str(a))
    return len(seen) + 1


assert solution(16) == 9
assert solution(103) == 4

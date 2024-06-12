def solution(n):
    return sum(int(digit) for digit in str(n))


assert solution(29) == 11

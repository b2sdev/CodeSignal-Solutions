def solution(n):
    digit_sum = str(n)
    degree = 0
    while len(digit_sum) > 1:
        degree += 1
        digit_sum = str(sum([int(d) for d in digit_sum]))
    return degree


assert solution(5) == 0
assert solution(100) == 1
assert solution(91) == 2

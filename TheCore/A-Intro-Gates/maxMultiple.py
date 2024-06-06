def solution(divisor, bound):
    num = bound
    while num > 1:
        if num % divisor == 0:
            return num
        num -= 1


assert solution(3, 10) == 9
assert solution(10, 50) == 50

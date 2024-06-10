def solution(a, b, n):
    money = 0
    while n > 0:
        money += a * b
        a += 1
        b += 1
        n -= 1
    return money


assert solution(1, 2, 2) == 8

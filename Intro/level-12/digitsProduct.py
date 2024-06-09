def solution(product):
    if product == 0:
        return 10
    if product == 1:
        return 1

    factors = []
    for divisor in range(9, 1, -1):
        while product % divisor == 0:
            product /= divisor
            factors.append(divisor)

    if product > 1:
        return -1

    return int("".join(map(str, factors[::-1])))


assert solution(12) == 26
assert solution(19) == -1
assert solution(450) == 2559
assert solution(0) == 10
assert solution(243) == 399

def solution(l, r):
    def sum_of_digits(a):
        total = 0
        while a > 0:
            total += a % 10
            a //= 10
        return total

    def sum_of_digits2(a):
        return sum(int(digit) for digit in str(a))

    count = 0
    for a in range(l, r + 1):
        for b in range(a + 1, r + 1):
            a_sum = sum_of_digits(a)
            b_sum = sum_of_digits(b)
            if b <= a + a_sum and a >= b - b_sum:
                count += 1
    return count


assert solution(10, 12) == 2
assert solution(1, 9) == 20
assert solution(12, 108) == 707
assert solution(239, 777) == 6166

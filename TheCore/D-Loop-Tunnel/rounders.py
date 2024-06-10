def solution(n):
    num = str(n)
    result = []
    carry = 0
    i = len(num) - 1
    while i > 0:
        digit = int(num[i]) + carry
        carry = 0
        if int(digit) >= 5:
            carry = 1
        result.append("0")
        i -= 1
    for k in str(int(num[i]) + carry)[::-1]:
        result.append(k)
    return int("".join(result[::-1]))


assert solution(15) == 20
assert solution(1234) == 1000
assert solution(1445) == 2000
assert solution(99) == 100

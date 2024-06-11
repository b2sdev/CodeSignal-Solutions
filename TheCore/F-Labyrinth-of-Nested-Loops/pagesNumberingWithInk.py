def solution(current, numberOfDigits):
    numbers = 0
    num = current
    while len(str(num)) + numbers <= numberOfDigits:
        numbers = numbers + len(str(num))
        num += 1
    return num - 1


assert solution(1, 5) == 5
assert solution(21, 5) == 22
assert solution(8, 4) == 10

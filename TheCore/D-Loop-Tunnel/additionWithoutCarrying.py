def solution(param1, param2):
    digits = max(len(str(param1)), len(str(param2)))
    p1, p2 = str(param1).zfill(digits), str(param2).zfill(digits)
    result = []
    for digit in range(digits):
        result.append((int(p1[digit]) + int(p2[digit])) % 10)
    return int("".join(map(str, result)))


assert solution(456, 1734) == 1180

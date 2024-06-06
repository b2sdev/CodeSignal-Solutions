def solution(a, b, c):
    if a + b == c:
        return True
    elif a - b == c:
        return True
    elif a * b == c:
        return True
    elif a / b == c:
        return True
    else:
        return False


assert solution(2, 3, 5) == True
assert solution(8, 2, 4) == True
assert solution(8, 3, 2) == False

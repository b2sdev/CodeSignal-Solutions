def solution(a, b):
    while a != b:
        a += 1
        b -= 1
        if a > b:
            return True
    return False

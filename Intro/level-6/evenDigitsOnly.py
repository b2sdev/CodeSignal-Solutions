def solution(n):
    for digit in str(n):
        if int(digit) % 2 != 0:
            return False
    return True


assert solution(248622) == True
assert solution(642386) == False

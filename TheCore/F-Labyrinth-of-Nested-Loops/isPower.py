def solution(n):
    if n == 1:
        return True
    for i in range(2, int(n**0.5) + 1):
        p = 2
        while i**p <= n:
            if i**p == n:
                return True
            p += 1
    return False


assert solution(125) == True
assert solution(72) == False
assert solution(324) == True

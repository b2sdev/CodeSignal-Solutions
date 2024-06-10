def solution(n):
    num = str(n)[::-1]
    roundness = 0
    left = 0
    right = 0
    if num[right] == "0":
        while right < len(num) and num[right] == "0":
            right += 1
        roundness = right - left
        left = right
    if right < len(num):
        right += 1
    while right < len(num) and num[right] != "0":
        right += 1
    return right < len(num) and right - left > 0


assert solution(902200100) == True
assert solution(11000) == False

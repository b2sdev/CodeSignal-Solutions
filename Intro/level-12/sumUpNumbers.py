def solution(inputString):
    total_sum = 0
    left = 0
    while left < len(inputString):
        while left < len(inputString) and not inputString[left].isnumeric():
            left += 1
        right = left
        while right < len(inputString) and inputString[right].isnumeric():
            right += 1
        if right - left > 0:
            total_sum += int(inputString[left:right])
        left = right
    return total_sum


assert solution("2 apples, 12 oranges") == 14
assert solution("Your payment method is invalid") == 0
assert solution("there are some (12) digits 5566 in this 770 string 239") == 6587

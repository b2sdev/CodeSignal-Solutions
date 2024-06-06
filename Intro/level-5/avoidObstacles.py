def solution(inputArray):
    inputArray.sort()
    max_jump = inputArray[-1] + 1
    jump = 1
    i = 0
    while i < max_jump:
        if i in inputArray:
            i = 0
            jump += 1
        else:
            i += jump
    return min(jump, max_jump)


assert solution([5, 3, 6, 7, 9]) == 4
assert solution([2, 3]) == 4

import math


def solution(inputArray):
    result = []
    for i in range(len(inputArray) - 1):
        result.append(abs(inputArray[i] - inputArray[i + 1]))
    return max(result)


assert solution([2, 4, 1, 0]) == 3

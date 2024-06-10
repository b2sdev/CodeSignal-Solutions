def solution(statues):
    result = 0
    statues.sort()
    for i in range(1, len(statues)):
        diff = statues[i] - statues[i - 1]
        if diff > 1:
            result += diff - 1
    return result


assert solution([6, 2, 3, 8]) == 3

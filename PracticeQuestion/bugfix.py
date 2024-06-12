def solution(a):

    indexOfMinimum = -1
    minimalSum = float("inf")

    for i in range(len(a)):
        curSum = 0
        for j in range(len(a)):
            curSum += abs(a[i] - a[j])
        if curSum < minimalSum:
            minimalSum = curSum
            indexOfMinimum = i

    return a[indexOfMinimum]


assert solution([2, 4, 7]) == 4
assert solution([2, 3]) == 2

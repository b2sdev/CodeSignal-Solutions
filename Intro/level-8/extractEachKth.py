def solution(inputArray, k):
    return [x for i, x in enumerate(inputArray) if (i + 1) % k != 0]


assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == [1, 2, 4, 5, 7, 8, 10]

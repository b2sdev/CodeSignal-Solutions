def solution(inputArray, l, r):
    left_end = l if l > 0 else 0
    right_start = r + 1 if r < len(inputArray) else r
    return inputArray[:left_end] + inputArray[right_start:]


assert solution([2, 3, 2, 3, 4, 5], 2, 4) == [2, 3, 5]
assert solution([2, 4, 10, 1], 0, 2) == [1]
assert solution([1, 1], 0, 1) == []
assert solution([0, -2, 5, 6], 3, 30) == [0, -2, 5]

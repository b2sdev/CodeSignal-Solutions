def solution(nums, k):
    seen = {}
    for i, n in enumerate(nums):
        if n not in seen:
            seen[n] = i
            continue
        if i - seen[n] <= k:
            return True
        seen[n] = i
    return False


assert solution([0, 1, 2, 3, 5, 2], 3) == True
assert solution([0, 1, 2, 3, 5, 2], 2) == False
assert solution([], 0) == False
assert solution([1, 0, 1, 1], 1) == True

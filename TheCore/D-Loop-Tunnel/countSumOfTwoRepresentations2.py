def solution(n, l, r):
    result = 0
    nums_set = set()
    for k in range(l, r + 1):
        if k * 2 == n:
            result += 1
        elif n - k in nums_set:
            result += 1
        nums_set.add(k)
    return result


assert solution(6, 2, 4) == 2

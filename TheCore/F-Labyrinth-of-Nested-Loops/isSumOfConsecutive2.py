def solution(n):
    result = 0
    psum = [0]
    for i in range(1, n + 1):
        psum.append(psum[i - 1] + i)
    print(psum)
    left, right = 0, 1
    while right <= n // 2 + 1:
        if psum[right] - psum[left] == n:
            result += 1
            left += 1
            right = left
        elif psum[right] - psum[left] > n:
            left += 1
            right = left
        right += 1
    print(n, result)
    return result


assert solution(9) == 2
assert solution(8) == 0
assert solution(15) == 3

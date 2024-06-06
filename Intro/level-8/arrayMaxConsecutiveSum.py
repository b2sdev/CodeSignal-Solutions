def solution(inputArray, k):
    max_sum = 0
    psum = [inputArray[0]]
    for i in range(1, len(inputArray)):
        psum.append(psum[i - 1] + inputArray[i])
    ans = []
    for i in range(len(psum) - 1, k - 1, -1):
        ans.append(psum[i] - psum[i - k])
    ans.append(psum[k - 1])
    return max(ans)


assert solution([2, 3, 5, 1, 6], 2) == 8
assert solution([3, 2, 1, 1], 1) == 3

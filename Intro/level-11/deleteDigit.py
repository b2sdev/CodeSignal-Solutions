def solution(n):
    s = str(n)
    size = len(s)
    nums = []
    for i in range(size):
        if i == 0:
            nums.append(s[1:])
        elif i == size - 1:
            nums.append(s[: size - 1])
        else:
            nums.append(s[:i] + s[i + 1 :])
    return max(map(int, nums))


assert solution(152) == 52
assert solution(1001) == 101

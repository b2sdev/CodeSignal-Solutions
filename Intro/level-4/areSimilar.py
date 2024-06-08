# https://app.codesignal.com/arcade/intro/level-4/xYXfzQmnhBvEKJwXP
def solution(a, b):
    if a == b:
        return True

    diff_indices = []
    for i in range(len(a)):
        if a[i] != b[i]:
            diff_indices.append(i)

    if len(diff_indices) != 2:
        return False

    i, j = diff_indices
    return a[i] == b[j] and a[j] == b[i]


assert solution([1, 2, 3], [1, 2, 3]) == True
assert solution([1, 2, 3], [2, 1, 3]) == True
assert solution([1, 2, 2], [2, 1, 1]) == False
assert solution([1, 2, 1, 2], [2, 2, 1, 1]) == True
assert (
    solution(
        [832, 998, 148, 570, 533, 561, 894, 147, 455, 279],
        [832, 570, 148, 998, 533, 561, 455, 147, 894, 279],
    )
    == False
)

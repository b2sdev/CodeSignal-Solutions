def solution(lastNumberOfDays):
    A = [31, 28, 31, 30, 31, 31]
    result = []
    for i in range(len(A) - 1):
        if A[i] == lastNumberOfDays:
            result.append(A[i + 1])
    print(result)
    return sorted(result)


assert solution(30) == [31]
assert solution(31) == [28, 30, 31]

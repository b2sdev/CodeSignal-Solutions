def solution(a):
    even = lambda x: x % 2 == 0
    result = [0, 0]
    i = 0
    while i < len(a):
        if even(i):
            result[0] += a[i]
        else:
            result[1] += a[i]
        i += 1
    return result


assert solution([50, 60, 60, 45, 70]) == [180, 105]

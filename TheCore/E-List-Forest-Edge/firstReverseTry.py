def solution(arr):
    if len(arr) < 2:
        return arr
    return [arr[-1]] + arr[1:-1] + [arr[0]]


assert solution([1, 2, 3, 4, 5]) == [5, 2, 3, 4, 1]
assert solution([]) == []
assert solution([239]) == [239]

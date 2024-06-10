def solution(arr):
    mid = len(arr) // 2
    middle = arr[mid]
    right_part = arr[mid + 1 :]
    if len(arr) % 2 == 0:
        middle += arr[mid - 1]
        left_part = arr[: mid - 1]
    else:
        left_part = arr[:mid]
    result = left_part + [middle] + right_part
    return result


assert solution([7, 2, 2, 5, 10, 7]) == [7, 2, 7, 10, 7]
assert solution([45, 23, 12, 33, 12, 453, -234, -45]) == [
    45,
    23,
    12,
    45,
    453,
    -234,
    -45,
]

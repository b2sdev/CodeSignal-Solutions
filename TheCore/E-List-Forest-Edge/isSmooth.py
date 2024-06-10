def solution(arr):
    if arr[0] != arr[-1]:
        return False
    mid = len(arr) // 2
    middle = arr[mid]
    if len(arr) % 2 == 0:
        middle += arr[mid - 1]
    return arr[0] == middle


assert solution([7, 2, 2, 5, 10, 7]) == True
assert solution([-5, -5, 10]) == False

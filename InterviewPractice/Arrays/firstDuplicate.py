def solution(a):
    n_set = set()
    for n in a:
        if n in n_set:
            return n
        n_set.add(n)
    return -1


assert solution([2, 1, 3, 5, 3, 2]) == 3
assert solution([2, 4, 3, 5, 1]) == -1

def solution(n):
    def count_ways(n, memo):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif memo[n] > -1:
            return memo[n]
        else:
            memo[n] = count_ways(n - 1, memo) + count_ways(n - 2, memo)
            return memo[n]

    memo = [-1 for _ in range(n + 1)]
    return count_ways(n, memo)


assert solution(1) == 1
assert solution(2) == 2
assert solution(38) == 63245986

def solution(n):
    dp = [0 for x in range(n + 1)]
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 2
    size = dp[n]
    for i in range(1, n + 1):
        left = right = (size - dp[i]) // 2
        k = dp[i]
        line = []
        while left > 0:
            line.append(" ")
            left -= 1
        while k > 0:
            line.append("*")
            k -= 1
        while right > 0:
            line.append(" ")
            right -= 1
        print("".join(line))


solution(3)
solution(5)

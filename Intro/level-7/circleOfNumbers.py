def solution(n, firstNumber):
    return (firstNumber % n + (n // 2)) % n


assert solution(10, 2) == 7

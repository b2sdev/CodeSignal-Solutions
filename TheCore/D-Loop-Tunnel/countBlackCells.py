def solution(n, m):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def line(x1, y1, x2, y2):
        return gcd(abs(x2 - x1), abs(y2 - y1))

    return n + m + line(n, m, 0, 0) - 2


assert solution(3, 4) == 6

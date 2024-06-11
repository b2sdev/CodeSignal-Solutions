def solution(n):
    def count_factors(n):
        factors = 0
        for i in range(1, n + 1):
            if n % i == 0:
                factors += 1
        return factors

    all_factors = [count_factors(num) for num in range(1, n + 1)]
    weaknesses = []
    for num, num_factors in enumerate(all_factors, 1):
        weakness = 0
        for factor in all_factors[:num]:
            if factor > num_factors:
                weakness += 1
        weaknesses.append(weakness)
    weakest = max(weaknesses)
    return [weakest, weaknesses.count(weakest)]


assert solution(9) == [2, 2]
assert solution(500) == [403, 1]

def solution(deposit, rate, threshold):
    year = 0
    while deposit < threshold:
        year += 1
        deposit += deposit * rate * 0.01
    return year


assert solution(100, 20, 170) == 3

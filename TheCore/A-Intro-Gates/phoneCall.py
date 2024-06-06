def solution(min1, min2_10, min11, s):
    if s < min1:
        return 0
    duration = 1
    s -= min1
    if s >= 9:
        duration += 9
        s -= min2_10 * 9
    else:
        while s > min2_10:
            duration += 1
            s -= min2_10
    if s > min11:
        duration += s // min11
    return duration


assert solution(3, 1, 2, 20) == 14
assert solution(1, 2, 1, 6) == 3
assert solution(10, 10, 10, 8) == 0

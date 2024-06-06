def solution(n):
    hh, mm = divmod(n, 60)
    hhmm = f"{hh:02d}{mm:02d}"
    return sum(int(x) for x in hhmm)


assert solution(240) == 4
assert solution(808) == 14

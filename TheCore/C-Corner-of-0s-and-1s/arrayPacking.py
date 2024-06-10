def solution(a):
    b = reversed([bin(n)[2:].zfill(8) for n in a])
    return int("".join(b), 2)


assert solution([24, 85, 0]) == 21784

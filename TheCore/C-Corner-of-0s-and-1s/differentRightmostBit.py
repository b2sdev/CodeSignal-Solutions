def solution(n, m):
    # return 2**next((i for i, (bit1, bit2) in enumerate(reversed(zip(bin(n)[2:].zfill(8), bin(m)[2:].zfill(8)))) if bit1 != bit2))
    return (n ^ m) & -(n ^ m)


assert solution(11, 13) == 2
assert solution(42, 22) == 4
assert solution(2**30, 16) == 9

def solution(n):
    return int(
        "".join([bin(n)[2:].zfill(32)[i : i + 2][::-1] for i in range(0, 32, 2)]), 2
    )


assert solution(13) == 14
assert solution(74) == 133

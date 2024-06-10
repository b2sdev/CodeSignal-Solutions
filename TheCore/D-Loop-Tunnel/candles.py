def solution(candlesNumber, makeNew):
    burned = [candlesNumber]
    burn = candlesNumber
    leftover = 0
    while leftover == 0 or burn + leftover >= makeNew:
        burn, leftover = divmod(burn + leftover, makeNew)
        burned.append(burn)
    return sum(burned)


assert solution(5, 2) == 9
assert solution(1, 2) == 1

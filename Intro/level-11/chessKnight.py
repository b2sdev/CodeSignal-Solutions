def solution(cell):
    in_board = lambda r, c: 0 <= r < 8 and 0 <= c < 8
    dir = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    moves = 0
    r, c = int(cell[1]) - 1, ord(cell[0]) - ord("a")
    for d in dir:
        nr, nc = r + d[0], c + d[1]
        if in_board(nr, nc):
            moves += 1
    return moves


assert solution("a1") == 2
assert solution("c2") == 6

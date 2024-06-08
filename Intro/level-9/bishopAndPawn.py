def solution(bishop, pawn):
    dir = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    in_board = lambda r, c: 0 < r <= 8 and 0 < c <= 8
    r, c = int(bishop[1]), ord(bishop[0]) - 96
    tr, tc = int(pawn[1]), ord(pawn[0]) - 96
    if r == tr and c == tc:
        return True
    for d in dir:
        nr, nc = r + d[0], c + d[1]
        while in_board(nr, nc):
            if nr == tr and nc == tc:
                return True
            nr, nc = nr + d[0], nc + d[1]
    return False


assert solution("a1", "c3") == True
assert solution("h1", "h3") == False

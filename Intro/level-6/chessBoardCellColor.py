def solution(cell1, cell2):
    def black(cell):
        r, c = ord(cell[0]) - ord("B"), int(cell[1])
        if r % 2 == 0:
            return True if c % 2 == 0 else False
        else:
            return False if c % 2 == 0 else True

    return black(cell1) == black(cell2)


assert solution("A1", "C3") == True
assert solution("A1", "H3") == False

def solution(crypt, solution):
    CODE = {}
    for ch, n in solution:
        CODE[ch] = n
    words = []
    for cr in crypt:
        words.append("".join([CODE[ch] for ch in cr]))
    for word in words:
        if len(word) > 1 and word[0] == "0":
            return False
    return int(words[0]) + int(words[1]) == int(words[2])


assert (
    solution(
        ["SEND", "MORE", "MONEY"],
        [
            ["O", "0"],
            ["M", "1"],
            ["Y", "2"],
            ["E", "5"],
            ["N", "6"],
            ["D", "7"],
            ["R", "8"],
            ["S", "9"],
        ],
    )
    == True
)
assert (
    solution(
        ["TEN", "TWO", "ONE"],
        [["O", "1"], ["T", "0"], ["W", "9"], ["E", "5"], ["N", "4"]],
    )
    == False
)
assert (
    solution(
        ["ONE", "ONE", "TWO"],
        [["O", "0"], ["T", "1"], ["W", "2"], ["E", "5"], ["N", "6"]],
    )
    == False
)

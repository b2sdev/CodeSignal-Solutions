import collections


def solution(s):
    counter = collections.Counter(s)
    candidates = [key for key, value in counter.items() if value == 1]
    for ch in s:
        if ch in candidates:
            return ch
    return "_"


assert solution("abacabad") == "c"
assert solution("abacabaabacaba") == "_"

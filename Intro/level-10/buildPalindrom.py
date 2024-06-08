def solution(st):
    is_palindrom = lambda s: s == s[::-1]
    if is_palindrom(st):
        return st
    for i in range(1, len(st)):
        if is_palindrom(st[i:]):
            return st + st[i - 1 :: -1]


assert solution("abcdc") == "abcdcba"
assert solution("abbcc") == "abbccbba"
assert solution("abaa") == "abaaba"
assert solution("abba") == "abba"
assert solution("ababab") == "abababa"

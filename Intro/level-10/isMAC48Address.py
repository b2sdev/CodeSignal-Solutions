def solution(inputString):
    if len(inputString) != 17:
        return False
    is_available = lambda ch: ch.isnumeric() or 65 <= ord(ch) <= 70
    i = 2
    while i <= len(inputString):
        if i < len(inputString) and inputString[i] != "-":
            return False
        if not is_available(inputString[i - 2]) or not is_available(inputString[i - 1]):
            return False
        i += 3
    return True


assert solution("1F-2G-GH-12-5A-66") == False
assert solution("Z1-1B-63-84-45-E6") == False
assert solution("02-03-04-05-06-07-") == False

def solution(inputString):
    i = 0
    while i < len(inputString):
        if inputString[i].isnumeric():
            return inputString[i]
        i += 1
    return ""


assert solution("var_1__Int") == "1"
assert solution("q2q-q") == "2"
assert solution("0ss") == "0"

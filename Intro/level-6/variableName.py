def solution(name):
    if name[0].isnumeric():
        return False
    for ch in name:
        if not ch.isalnum() and ch != "_":
            return False
    return True


assert solution("var_1__Int") == True
assert solution("qq-q") == False
assert solution("2w2") == False

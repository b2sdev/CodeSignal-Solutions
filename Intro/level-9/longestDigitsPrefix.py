def solution(inputString):
    prefix = []
    for ch in inputString:
        if not ch.isdigit():
            break
        prefix.append(ch)
    return ''.join(prefix)


assert solution("123aa1") == "123"

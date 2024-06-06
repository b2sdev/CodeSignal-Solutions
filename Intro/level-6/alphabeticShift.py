def solution(inputString):
    inputString = inputString.replace("z", "`")
    result = [chr(ord(ch) + 1) for ch in inputString]
    return "".join(result)


assert solution("crazy") == "dsbaz"

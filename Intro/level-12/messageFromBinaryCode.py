def solution(code):
    codes = []
    i = 0
    while i + 8 <= len(code):
        codes.append(chr(int(code[i : i + 8], 2)))
        i += 8
    return "".join(codes)


assert solution("010010000110010101101100011011000110111100100001") == "Hello!"

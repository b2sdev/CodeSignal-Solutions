def solution(s):
    encoding = []
    left, right = 0, 0
    while right < len(s):
        ch = s[right]
        while right + 1 < len(s) and s[right + 1] == ch:
            right += 1

        encoding.append(str(right - left + 1) + ch if right - left > 0 else ch)
        left = right = right + 1
        if right < len(s):
            ch = s[right]

    return "".join(encoding)


def solution2(s):
    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += str(count) + s[i - 1] if count > 1 else s[i - 1]
            count = 1

    result += str(count) + s[-1] if count > 1 else s[-1]

    return result


assert solution("aabbbc") == "2a3bc"

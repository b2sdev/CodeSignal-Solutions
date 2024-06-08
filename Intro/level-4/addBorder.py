# https://app.codesignal.com/arcade/intro/level-4/ZCD7NQnED724bJtjN
def solution(picture):
    width = len(picture[0]) + 2
    border = "*" * width
    result = [border]
    for line in picture:
        result.append("*" + line + "*")
    result.append(border)
    return result


assert solution(["abc", "ded"]) == ["*****", "*abc*", "*ded*", "*****"]

# Time complexity: O(n)
# Space complexity: O(n)

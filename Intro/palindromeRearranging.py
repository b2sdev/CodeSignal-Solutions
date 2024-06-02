# https://app.codesignal.com/arcade/intro/level-4/Xfeo7r9SBSpo3Wico
def solution(inputString):
    char_count = {}
    for char in inputString:
        char_count[char] = char_count.get(char, 0) + 1

    odd_count = 0
    for count in char_count.values():
        if count % 2 == 1:
            odd_count += 1

    return odd_count <= 1


assert solution("aabb") == True
assert solution("abacb") == True
assert solution("a") == True
assert solution("aaabbbc") == True

# Time complexity: O(n)
# Space complexity: O(n)
